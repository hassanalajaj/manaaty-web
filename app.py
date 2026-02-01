# app.py
import streamlit as st
import pandas as pd
import numpy as np
import os
from config import CUSTOM_CSS, LOW_PRESET, MODERATE_PRESET, HIGH_PRESET, CLINICAL_RECOMMENDATIONS
from ml_engine import load_and_train_model, compute_slope
from plots import plot_shap_analysis, plot_vital_trends

# --- Page Setup ---
st.set_page_config(page_title="Manaaty – AI Risk System", layout="wide", page_icon="🧬")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- Session Initialization ---
def init_session():
    # Load defaults if not set
    if "age" not in st.session_state:
        for k, v in LOW_PRESET.items():
            st.session_state[k] = v

def apply_preset(preset):
    for k, v in preset.items():
        st.session_state[k] = v
    st.rerun()

init_session()

# --- Header & Logo ---
c1, c2 = st.columns([4, 1])
with c1:
    st.title("🧬 Early Immune Activation Dashboard")
    st.caption("Clinical Prototype – Manaaty AI System")
with c2:
    # ⚠️ Displays logo.png if present
    if os.path.exists("logo.png"):
        st.image("logo.png", width=160)
    else:
        st.write("") 

# --- Load Model ---
with st.spinner("🔄 Initializing AI Engine & Training Models..."):
    model, base_model, metrics, feature_cols = load_and_train_model()

# --- Sidebar ---
st.sidebar.title("🩺 Controls")

st.sidebar.subheader("📊 Model Accuracy")
m1, m2 = st.sidebar.columns(2)
with m1: st.metric("Accuracy", f"{metrics['accuracy']*100:.1f}%")
with m2: st.metric("Recall", f"{metrics['classification_report']['weighted avg']['recall']*100:.1f}%")
st.sidebar.caption(f"Valid. F1: {metrics['cv_mean']:.3f} ± {metrics['cv_std']:.3f}")

st.sidebar.markdown("---")
st.sidebar.subheader("Presets")
b1, b2, b3 = st.sidebar.columns(3)
if b1.button("Low"): apply_preset(LOW_PRESET)
if b2.button("Med"): apply_preset(MODERATE_PRESET)
if b3.button("High"): apply_preset(HIGH_PRESET)

# --- Inputs (Mapped to Session State & CSV Columns) ---
st.sidebar.markdown("---")
st.sidebar.subheader("Patient Data")

# Using 'key' connects the widget directly to session_state
age = st.sidebar.number_input("Age", 0, 110, key="age")

st.sidebar.markdown("**Biomarkers**")
# Keys match Config & CSV exactly
crp = st.sidebar.number_input("CRP (mg/L)", 0.0, 300.0, key="baseline_crp_mg_l", step=0.1)
il6 = st.sidebar.number_input("IL-6 (pg/mL)", 0.0, 1000.0, key="baseline_il6_pg_ml", step=0.1)
tnf = st.sidebar.number_input("TNF-α (pg/mL)", 0.0, 1000.0, key="baseline_tnf_alpha_pg_ml", step=0.1)
ferritin = st.sidebar.number_input("Ferritin (ng/mL)", 0.0, 2000.0, key="baseline_ferritin_ng_ml", step=1.0)
lymph = st.sidebar.number_input("Lymphocytes (%)", 0.0, 100.0, key="baseline_lymph_pct", step=0.1)
neutro = st.sidebar.number_input("Neutrophils (%)", 0.0, 100.0, key="baseline_neutro_pct", step=0.1)

st.sidebar.markdown("**Vitals (Baseline -> Last 24h)**")
base_temp = st.sidebar.number_input("Base Temp (°C)", 35.0, 42.0, key="baseline_temp_c", step=0.1)
last_temp = st.sidebar.number_input("Last Temp (24h)", 35.0, 42.0, key="last_temp", step=0.1)

base_hr = st.sidebar.number_input("Base HR (bpm)", 30, 220, key="baseline_hr_bpm")
last_hr = st.sidebar.number_input("Last HR (24h)", 30, 220, key="last_hr")

base_spo2 = st.sidebar.number_input("Base SpO2 (%)", 70.0, 100.0, key="baseline_spo2", step=0.1)
last_spo2 = st.sidebar.number_input("Last SpO2 (24h)", 70.0, 100.0, key="last_spo2", step=0.1)

base_rr = st.sidebar.number_input("Base RR (bpm)", 5, 60, key="baseline_rr_bpm")
last_rr = st.sidebar.number_input("Last RR (24h)", 5, 60, key="last_rr")

base_hrv = st.sidebar.number_input("Base HRV (ms)", 0.0, 300.0, key="baseline_hrv_rmssd_ms", step=1.0)
last_hrv = st.sidebar.number_input("Last HRV (24h)", 0.0, 300.0, key="last_hrv", step=1.0)

base_act = st.sidebar.number_input("Base Activity (0-1)", 0.0, 1.0, key="baseline_activity_index", step=0.01)
last_act = st.sidebar.number_input("Last Activity (24h)", 0.0, 1.0, key="last_activity", step=0.01)

# --- Main Logic ---
col_L, col_R = st.columns([1, 2])

with col_L:
    st.markdown('<div class="m-card">', unsafe_allow_html=True)
    st.subheader("📋 Live Summary")
    st.info(f"🌡️ Temp: {last_temp:.1f}°C")
    st.info(f"💓 HR: {last_hr} bpm")
    st.info(f"🔬 CRP: {crp:.1f} mg/L")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔍 Run Analysis", type="primary", use_container_width=True):
        # 1. Calculate Slopes
        temp_slope = compute_slope(base_temp, last_temp)
        hr_slope = compute_slope(base_hr, last_hr)
        spo2_slope = compute_slope(base_spo2, last_spo2)
        rr_slope = compute_slope(base_rr, last_rr)
        hrv_slope = compute_slope(base_hrv, last_hrv)
        act_slope = compute_slope(base_act, last_act)
        
        # 2. Prepare Data Row (Must match CSV feature_cols exactly)
        input_data = {
            "age": age,
            "baseline_temp_c": base_temp,
            "baseline_hr_bpm": base_hr,
            "baseline_hrv_rmssd_ms": base_hrv,
            "baseline_spo2": base_spo2,
            "baseline_rr_bpm": base_rr,
            "baseline_activity_index": base_act,
            "baseline_crp_mg_l": crp,
            "baseline_il6_pg_ml": il6,
            "baseline_tnf_alpha_pg_ml": tnf,
            "baseline_ferritin_ng_ml": ferritin,
            "baseline_lymph_pct": lymph,
            "baseline_neutro_pct": neutro,
            # Slopes
            "temp_slope_0_24": temp_slope,
            "hr_slope_0_24": hr_slope,
            "spo2_slope_0_24": spo2_slope,
            "hrv_slope_0_24": hrv_slope,
            "rr_slope_0_24": rr_slope,
            "activity_slope_0_24": act_slope,
        }
        
        input_df = pd.DataFrame([input_data])
        
        try:
            # 3. Predict
            pred = int(model.predict(input_df)[0])
            probs = model.predict_proba(input_df)[0]
            
            # 4. Display Results
            with col_R:
                if pred == 2:
                    st.markdown('<div class="urgent-alert"><h2>⚠️ HIGH RISK DETECTED</h2></div>', unsafe_allow_html=True)
                
                risk_map = {0: ("Low", "risk-low"), 1: ("Moderate", "risk-mod"), 2: ("High", "risk-high")}
                lbl, css = risk_map[pred]
                
                st.markdown(f'<div class="m-card risk-card {css}"><h3>{lbl} Risk Level ({probs[pred]*100:.1f}%)</h3></div>', unsafe_allow_html=True)

                st.markdown("### 📝 Clinical Actions")
                for rec in CLINICAL_RECOMMENDATIONS[pred]:
                    st.write(rec)

                st.markdown("### 🔍 Analysis")
                tab1, tab2 = st.tabs(["Feature Impact (SHAP)", "Vital Trends"])
                
                with tab1:
                    fig_shap, _ = plot_shap_analysis(base_model, input_df, pred, feature_cols)
                    if fig_shap: st.plotly_chart(fig_shap, use_container_width=True)
                
                with tab2:
                    base_vitals = {'temp': base_temp, 'hr': base_hr, 'rr': base_rr, 'spo2': base_spo2}
                    last_vitals = {'temp': last_temp, 'hr': last_hr, 'rr': last_rr, 'spo2': last_spo2}
                    st.plotly_chart(plot_vital_trends(base_vitals, last_vitals, pred), use_container_width=True)

        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")
            st.write("Input columns:", input_df.columns.tolist())
    else:
        with col_R:
            st.info("👈 Please adjust values in the sidebar and click 'Run Analysis'")
