# app.py
import streamlit as st
import pandas as pd
import numpy as np
import os
from config import CUSTOM_CSS, LOW_PRESET, MODERATE_PRESET, HIGH_PRESET, PATIENT_GUIDANCE
from ml_engine import load_and_train_model, compute_slope
from plots import plot_shap_analysis, plot_vital_trends

# --- Mobile-Like Configuration ---
st.set_page_config(page_title="Manaaty Mobile", layout="centered", page_icon="🧬") # Centered layout mimics phone
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- Session Init ---
def init_session():
    if "age" not in st.session_state:
        for k, v in LOW_PRESET.items():
            st.session_state[k] = v

def apply_preset(preset):
    for k, v in preset.items():
        st.session_state[k] = v
    st.rerun()

init_session()

# --- Load Model ---
with st.spinner("Connecting to Patch..."):
    model, base_model, metrics, feature_cols = load_and_train_model()

# ==========================================
# 📱 MOBILE INTERFACE START
# ==========================================

# 1. Header (Simple & Clean)
st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>🧬 Manaaty</h2>", unsafe_allow_html=True)

# 2. Main Status Card (The "Hero" Section)
# This mimics receiving data from the device
st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("Heart Rate", f"{st.session_state['last_hr']} bpm", "Normal")
c2.metric("Temp", f"{st.session_state['last_temp']:.1f} °C", "Stable")
c3.metric("SpO2", f"{st.session_state['last_spo2']:.0f}%", "Good")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Analyze Button (Big & Clickable)
if st.button("🔄 SCAN HEALTH STATUS"):
    
    # --- Prepare Data (Hidden logic) ---
    temp_slope = compute_slope(st.session_state['baseline_temp_c'], st.session_state['last_temp'])
    hr_slope = compute_slope(st.session_state['baseline_hr_bpm'], st.session_state['last_hr'])
    spo2_slope = compute_slope(st.session_state['baseline_spo2'], st.session_state['last_spo2'])
    rr_slope = compute_slope(st.session_state['baseline_rr_bpm'], st.session_state['last_rr'])
    hrv_slope = compute_slope(st.session_state['baseline_hrv_rmssd_ms'], st.session_state['last_hrv'])
    act_slope = compute_slope(st.session_state['baseline_activity_index'], st.session_state['last_activity'])
    
    input_data = {
        "age": st.session_state['age'],
        "baseline_temp_c": st.session_state['baseline_temp_c'],
        "baseline_hr_bpm": st.session_state['baseline_hr_bpm'],
        "baseline_hrv_rmssd_ms": st.session_state['baseline_hrv_rmssd_ms'],
        "baseline_spo2": st.session_state['baseline_spo2'],
        "baseline_rr_bpm": st.session_state['baseline_rr_bpm'],
        "baseline_activity_index": st.session_state['baseline_activity_index'],
        "baseline_crp_mg_l": st.session_state['baseline_crp_mg_l'],
        "baseline_il6_pg_ml": st.session_state['baseline_il6_pg_ml'],
        "baseline_tnf_alpha_pg_ml": st.session_state['baseline_tnf_alpha_pg_ml'],
        "baseline_ferritin_ng_ml": st.session_state['baseline_ferritin_ng_ml'],
        "baseline_lymph_pct": st.session_state['baseline_lymph_pct'],
        "baseline_neutro_pct": st.session_state['baseline_neutro_pct'],
        "temp_slope_0_24": temp_slope, "hr_slope_0_24": hr_slope,
        "spo2_slope_0_24": spo2_slope, "hrv_slope_0_24": hrv_slope,
        "rr_slope_0_24": rr_slope, "activity_slope_0_24": act_slope,
    }
    input_df = pd.DataFrame([input_data])
    
    # --- Predict ---
    pred = int(model.predict(input_df)[0])
    
    # --- RESULT DISPLAY (Patient Centric) ---
    guidance = PATIENT_GUIDANCE[pred]
    status_class = ["status-low", "status-mod", "status-high"][pred]
    
    st.markdown(f"""
        <div class="mobile-card" style="text-align: center;">
            <div class="status-badge {status_class}">Status Update</div>
            <h1 style="margin: 10px 0;">{guidance['title']}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # --- ACTION PLAN (The "What should I do?" part) ---
    st.markdown("### 👉 Your Action Plan")
    st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
    
    for i, step in enumerate(guidance['steps'], 1):
        st.markdown(f"""
            <div class="step-box">
                <span class="step-number">{i}.</span> {step}
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

    # --- DEEP DIVE (Optional Details) ---
    with st.expander("Show Detailed Charts"):
        tab1, tab2 = st.tabs(["Why This Result?", "Trends"])
        
        with tab1:
            fig_shap, _ = plot_shap_analysis(base_model, input_df, pred, feature_cols)
            if fig_shap: st.plotly_chart(fig_shap, use_container_width=True)
        
        with tab2:
            base_vitals = {'temp': st.session_state['baseline_temp_c'], 'hr': st.session_state['baseline_hr_bpm'], 'rr': st.session_state['baseline_rr_bpm'], 'spo2': st.session_state['baseline_spo2']}
            last_vitals = {'temp': st.session_state['last_temp'], 'hr': st.session_state['last_hr'], 'rr': st.session_state['last_rr'], 'spo2': st.session_state['last_spo2']}
            st.plotly_chart(plot_vital_trends(base_vitals, last_vitals, pred), use_container_width=True)

else:
    st.info("👆 Tap the button above to analyze your patch data.")


# ==========================================
# 🛠️ SIDEBAR (DEV CONTROLS - Hidden Logic)
# ==========================================
# We keep inputs here for simulation, but pretend they come from the device
st.sidebar.header("🛠️ Simulation Controls")
st.sidebar.caption("Use these to simulate patch data")

st.sidebar.subheader("Quick Sim")
c1, c2, c3 = st.sidebar.columns(3)
if c1.button("🟢"): apply_preset(LOW_PRESET)
if c2.button("🟡"): apply_preset(MODERATE_PRESET)
if c3.button("🔴"): apply_preset(HIGH_PRESET)

st.sidebar.markdown("---")
# Inputs hidden in sidebar to keep main UI clean
# Using correct keys to match session state and config
st.sidebar.number_input("Temp (Last)", 35.0, 42.0, key="last_temp", step=0.1)
st.sidebar.number_input("HR (Last)", 30, 220, key="last_hr")
st.sidebar.number_input("SpO2", 70.0, 100.0, key="last_spo2", step=0.1)
st.sidebar.number_input("CRP", 0.0, 300.0, key="baseline_crp_mg_l", step=0.1)

# Hidden Inputs (We need them for the model, but user doesn't need to adjust them constantly)
with st.sidebar.expander("Advanced Biomarkers"):
    st.number_input("Age", 0, 110, key="age")
    st.number_input("IL-6", 0.0, 1000.0, key="baseline_il6_pg_ml")
    st.number_input("TNF", 0.0, 1000.0, key="baseline_tnf_alpha_pg_ml")
    st.number_input("Ferritin", 0.0, 2000.0, key="baseline_ferritin_ng_ml")
    st.number_input("Lymph", 0.0, 100.0, key="baseline_lymph_pct")
    st.number_input("Neutro", 0.0, 100.0, key="baseline_neutro_pct")
    st.number_input("Base Temp", 35.0, 42.0, key="baseline_temp_c")
    st.number_input("Base HR", 30, 220, key="baseline_hr_bpm")
    st.number_input("Base SpO2", 70.0, 100.0, key="baseline_spo2")
    st.number_input("Base RR", 5, 60, key="baseline_rr_bpm")
    st.number_input("Last RR", 5, 60, key="last_rr")
    st.number_input("Base HRV", 0.0, 300.0, key="baseline_hrv_rmssd_ms")
    st.number_input("Last HRV", 0.0, 300.0, key="last_hrv")
    st.number_input("Base Act", 0.0, 1.0, key="baseline_activity_index")
    st.number_input("Last Act", 0.0, 1.0, key="last_activity")
