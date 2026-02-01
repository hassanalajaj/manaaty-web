# ml_engine.py
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

@st.cache_resource
def load_and_train_model():
    # ⚠️ IMPORTANT: Ensure your CSV is renamed to this:
    data_path = "patient_data.csv"
    
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"❌ Error: File '{data_path}' not found. Please rename your uploaded CSV to 'patient_data.csv'.")
        st.stop()

    # Exact columns from your specific CSV file
    feature_cols = [
        "age", "baseline_temp_c", "baseline_hr_bpm", "baseline_hrv_rmssd_ms",
        "baseline_spo2", "baseline_rr_bpm", "baseline_activity_index",
        "baseline_crp_mg_l", "baseline_il6_pg_ml", "baseline_tnf_alpha_pg_ml",
        "baseline_ferritin_ng_ml", "baseline_lymph_pct", "baseline_neutro_pct",
        "temp_slope_0_24", "hr_slope_0_24", "spo2_slope_0_24",
        "hrv_slope_0_24", "rr_slope_0_24", "activity_slope_0_24",
    ]

    # Verify columns exist
    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        st.error(f"❌ Missing columns in CSV: {missing}")
        st.stop()

    X = df[feature_cols]
    y = df["early_risk_class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Models
    rf = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1, class_weight="balanced", max_depth=15)
    xgb = XGBClassifier(n_estimators=300, random_state=42, n_jobs=-1, max_depth=10, learning_rate=0.1)
    gb = GradientBoostingClassifier(n_estimators=200, random_state=42, max_depth=8)
    
    model = VotingClassifier(
        estimators=[('rf', rf), ('xgb', xgb), ('gb', gb)],
        voting='soft', weights=[1, 2, 1]
    )
    
    model.fit(X_train, y_train)
    
    # Validation Metrics
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'cv_mean': cross_val_score(rf, X, y, cv=5, scoring='f1_weighted').mean(),
        'cv_std': cross_val_score(rf, X, y, cv=5, scoring='f1_weighted').std(),
        'confusion_matrix': confusion_matrix(y_test, y_pred),
        'classification_report': classification_report(y_test, y_pred, output_dict=True)
    }

    base_model = rf.fit(X_train, y_train)

    return model, base_model, metrics, feature_cols

def compute_slope(baseline: float, last: float, hours: float = 24.0) -> float:
    try:
        return (float(last) - float(baseline)) / float(hours)
    except:
        return 0.0
