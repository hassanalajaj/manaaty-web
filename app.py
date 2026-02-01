# app.py
import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
# تأكد أن config.py يحتوي على المتغيرات المطلوبة
from config import CUSTOM_CSS, LOW_PRESET, MODERATE_PRESET, HIGH_PRESET, CLINICAL_ACTIONS
from ml_engine import load_and_train_model, compute_slope
from plots import plot_shap_analysis, plot_vital_trends

# ==================== CONFIG ====================
st.set_page_config(
    page_title="Manaaty",
    layout="centered",
    page_icon="🧬",
    initial_sidebar_state="collapsed"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ==================== SESSION MANAGEMENT (FIXED) ====================
def init_session():
    # 1. التأكد من تحميل بيانات المريض الافتراضية (Preset)
    # الفحص هنا يتم على مفتاح حيوي مثل 'last_temp' لضمان تحميل البيانات
    if "last_temp" not in st.session_state:
        for k, v in MODERATE_PRESET.items():
            st.session_state[k] = v

    # 2. التأكد من تحميل إعدادات التطبيق
    if "patient_name" not in st.session_state:
        st.session_state.patient_name = "أحمد محمد"
        st.session_state.language = "ar"
        st.session_state.last_check = datetime.now() - timedelta(hours=2)
        st.session_state.device_battery = 87
        st.session_state.device_days_remaining = 4

def toggle_language():
    st.session_state.language = "en" if st.session_state.language == "ar" else "ar"
    st.rerun()

# استدعاء الدالة لتهيئة الجلسة
init_session()

# تعريف متغير اللغة لتسهيل الاستخدام
lang = st.session_state.language

# ==================== LOAD MODEL ====================
# استخدام التخزين المؤقت لتسريع التحميل
@st.cache_resource
def get_model():
    return load_and_train_model()

with st.spinner("جاري الاتصال بالجهاز..."):
    model, base_model, metrics, feature_cols = get_model()

# ==================== HEADER ====================
st.markdown(f"""
<div style="text-align: center; margin-bottom: 20px;">
    <div style="font-size: 50px;">🧬</div>
    <h1 style="margin:0;">{'مناعتي' if lang == 'ar' else 'Manaaty'}</h1>
    <p style="color: #8892b8;">{'نظام الحماية الذكي' if lang == 'ar' else 'Smart Protection System'}</p>
</div>
""", unsafe_allow_html=True)

if st.button("🌐 " + ("English" if lang == "ar" else "عربي"), key="lang_btn"):
    toggle_language()

# ==================== DEVICE INFO ====================
st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("Battery", f"{st.session_state.device_battery}%", "Good")
c2.metric("Next Read", "2h", "Auto")
c3.metric("Patch", "Active", "OK")
st.markdown('</div>', unsafe_allow_html=True)

# ==================== SIMULATION CONTROLS ====================
# أزرار المحاكاة (مهمة للتجربة)
st.markdown('<div class="mobile-card" style="border: 1px dashed #444;">', unsafe_allow_html=True)
st.caption("🛠️ محاكاة النتائج (اضغط لتجربة حالات مختلفة):")
b1, b2, b3 = st.columns(3)
if b1.button("✅ طبيعي"):
    for k, v in LOW_PRESET.items(): st.session_state[k] = v
    st.rerun()
if b2.button("⚠️ متوسط"):
    for k, v in MODERATE_PRESET.items(): st.session_state[k] = v
    st.rerun()
if b3.button("🚨 خطر"):
    for k, v in HIGH_PRESET.items(): st.session_state[k] = v
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ==================== VITALS DISPLAY ====================
st.markdown(f"### {'مؤشراتك الحيوية' if lang == 'ar' else 'Current Vitals'}")

def get_css_class(val, low, high):
    if val < low or val > high: return "vital-row critical"
    if val < low*1.1 or val > high*0.9: return "vital-row elevated"
    return "vital-row"

# التأكد من وجود القيم قبل عرضها (حماية إضافية)
current_temp = st.session_state.get('last_temp', 37.0)
current_hr = st.session_state.get('last_hr', 75)
current_spo2 = st.session_state.get('last_spo2', 98)

vitals = [
    ("🌡️", "Temp", current_temp, "°C", 36, 37.5),
    ("💓", "Heart", current_hr, "bpm", 60, 100),
    ("🫁", "SpO2", current_spo2, "%", 95, 100),
]

st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
for icon, label, val, unit, low, high in vitals:
    css = get_css_class(val, low, high)
    lbl = label if lang == 'en' else {'Temp':'الحرارة', 'Heart':'النبض', 'SpO2':'الأكسجين'}[label]
    st.markdown(f"""
    <div class="{css}">
        <div class="vital-label"><span>{icon}</span> {lbl}</div>
        <div class="vital-value">{val:.1f} <small>{unit}</small></div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================== ACTION BUTTON & LOGIC ====================
if st.button("🔍 " + ("تحليل الحالة الآن" if lang == "ar" else "Analyze Health Status"), type="primary"):
    
    # 1. Prepare Data using Session State
    # استخدام .get لتجنب الأخطاء في حال غياب قيمة
    temp_slope = compute_slope(st.session_state.get('baseline_temp_c', 37), st.session_state.get('last_temp', 37))
    hr_slope = compute_slope(st.session_state.get('baseline_hr_bpm', 70), st.session_state.get('last_hr', 70))
    spo2_slope = compute_slope(st.session_state.get('baseline_spo2', 98), st.session_state.get('last_spo2', 98))
    rr_slope = compute_slope(st.session_state.get('baseline_rr_bpm', 14), st.session_state.get('last_rr', 14))
    hrv_slope = compute_slope(st.session_state.get('baseline_hrv_rmssd_ms', 50), st.session_state.get('last_hrv', 50))
    act_slope = compute_slope(st.session_state.get('baseline_activity_index', 0.5), st.session_state.get('last_activity', 0.5))
    
    input_data = {
        "age": st.session_state.get('age', 30),
        "baseline_temp_c": st.session_state.get('baseline_temp_c', 37),
        "baseline_hr_bpm": st.session_state.get('baseline_hr_bpm', 70),
        "baseline_hrv_rmssd_ms": st.session_state.get('baseline_hrv_rmssd_ms', 50),
        "baseline_spo2": st.session_state.get('baseline_spo2', 98),
        "baseline_rr_bpm": st.session_state.get('baseline_rr_bpm', 14),
        "baseline_activity_index": st.session_state.get('baseline_activity_index', 0.5),
        "baseline_crp_mg_l": st.session_state.get('baseline_crp_mg_l', 1.0),
        "baseline_il6_pg_ml": st.session_state.get('baseline_il6_pg_ml', 2.0),
        "baseline_tnf_alpha_pg_ml": st.session_state.get('baseline_tnf_alpha_pg_ml', 5.0),
        "baseline_ferritin_ng_ml": st.session_state.get('baseline_ferritin_ng_ml', 100),
        "baseline_lymph_pct": st.session_state.get('baseline_lymph_pct', 30),
        "baseline_neutro_pct": st.session_state.get('baseline_neutro_pct', 60),
        "temp_slope_0_24": temp_slope, "hr_slope_0_24": hr_slope,
        "spo2_slope_0_24": spo2_slope, "hrv_slope_0_24": hrv_slope,
        "rr_slope_0_24": rr_slope, "activity_slope_0_24": act_slope,
    }
    input_df = pd.DataFrame([input_data])
    
    # 2. Predict
    try:
        pred_class = int(model.predict(input_df)[0])
        pred_proba = model.predict_proba(input_df)[0]
        action = CLINICAL_ACTIONS[pred_class]
        
        # 3. RESULT CARD
        st.markdown('<div class="mobile-card" style="text-align:center;">', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="status-badge {action['badge']}">
            {action['icon']} {action['title'] if lang == 'ar' else action['title_en']}
        </div>
        <h2 style="margin:10px 0;">{action['message'] if lang == 'ar' else action['message_en']}</h2>
        <p style="color:#667eea; font-weight:bold;">Trust Score: {pred_proba[pred_class]*100:.0f}%</p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 4. INSTRUCTIONS
        st.markdown(f"### {'الخطوات القادمة' if lang == 'ar' else 'Next Steps'}")
        st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
        instrs = action['instructions']['ar'] if lang == 'ar' else action['instructions']['en']
        for ins in instrs:
            st.markdown(f"**{ins}**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 5. ACTION BUTTONS
        for btn in action['action_buttons']:
            lbl = btn['label'] if lang == 'ar' else btn['label_en']
            cls = 'action-btn-emergency' if btn['type'] == 'emergency' else 'action-btn'
            st.markdown(f'<div class="{cls}">{lbl}</div>', unsafe_allow_html=True)

        # 6. CHARTS EXPANDER
        with st.expander("📊 " + ("تفاصيل أكثر" if lang == 'ar' else "More Details")):
            # Vital Trends
            base_vitals = {'temp': st.session_state.get('baseline_temp_c', 37), 'hr': st.session_state.get('baseline_hr_bpm', 70)}
            last_vitals = {'temp': st.session_state.get('last_temp', 37), 'hr': st.session_state.get('last_hr', 70)}
            st.plotly_chart(plot_vital_trends(base_vitals, last_vitals, pred_class), use_container_width=True)
            
            # SHAP
            fig_shap, _ = plot_shap_analysis(base_model, input_df, pred_class, feature_cols)
            if fig_shap: st.plotly_chart(fig_shap, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
