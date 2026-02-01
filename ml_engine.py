# ml_engine.py
import streamlit as st
import pandas as pd
import os
import joblib  # مكتبة للحفظ والاسترجاع السريع
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# اسم ملف الموديل المحفوظ
MODEL_FILE = "manaaty_model_v1.pkl"

@st.cache_resource
def load_and_train_model():
    # 1. الخطة أ: محاولة تحميل الموديل الجاهز فوراً
    if os.path.exists(MODEL_FILE):
        print("⚡ Loading saved model from disk...")
        saved_data = joblib.load(MODEL_FILE)
        return (saved_data['model'], 
                saved_data['base_model'], 
                saved_data['metrics'], 
                saved_data['feature_cols'])

    # 2. الخطة ب: الموديل غير موجود؟ ندربه الآن (للمرة الأولى فقط)
    print("🐢 No saved model found. Training now...")
    
    data_path = "patient_data.csv"
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"❌ Error: File '{data_path}' not found.")
        st.stop()

    feature_cols = [
        "age", "baseline_temp_c", "baseline_hr_bpm", "baseline_hrv_rmssd_ms",
        "baseline_spo2", "baseline_rr_bpm", "baseline_activity_index",
        "baseline_crp_mg_l", "baseline_il6_pg_ml", "baseline_tnf_alpha_pg_ml",
        "baseline_ferritin_ng_ml", "baseline_lymph_pct", "baseline_neutro_pct",
        "temp_slope_0_24", "hr_slope_0_24", "spo2_slope_0_24",
        "hrv_slope_0_24", "rr_slope_0_24", "activity_slope_0_24",
    ]

    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        st.error(f"❌ Missing columns: {missing}")
        st.stop()

    X = df[feature_cols]
    y = df["early_risk_class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Training
    rf = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1, class_weight="balanced", max_depth=15)
    xgb = XGBClassifier(n_estimators=300, random_state=42, n_jobs=-1, max_depth=10, learning_rate=0.1)
    gb = GradientBoostingClassifier(n_estimators=200, random_state=42, max_depth=8)
    
    model = VotingClassifier(
        estimators=[('rf', rf), ('xgb', xgb), ('gb', gb)],
        voting='soft', weights=[1, 2, 1]
    )
    
    model.fit(X_train, y_train)
    
    # Metrics
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'cv_mean': cross_val_score(rf, X, y, cv=5, scoring='f1_weighted').mean(),
        'cv_std': cross_val_score(rf, X, y, cv=5, scoring='f1_weighted').std(),
        'confusion_matrix': confusion_matrix(y_test, y_pred),
        'classification_report': classification_report(y_test, y_pred, output_dict=True)
    }

    base_model = rf.fit(X_train, y_train)

    # 3. حفظ كل شيء في ملف واحد
    package = {
        'model': model,
        'base_model': base_model,
        'metrics': metrics,
        'feature_cols': feature_cols
    }
    joblib.dump(package, MODEL_FILE)
    print("✅ Model saved successfully!")

    return model, base_model, metrics, feature_cols

def compute_slope(baseline: float, last: float, hours: float = 24.0) -> float:
    try:
        return (float(last) - float(baseline)) / float(hours)
    except:
        return 0.0
