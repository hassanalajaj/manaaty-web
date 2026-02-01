# app.py
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import os
import base64
from datetime import datetime, timedelta
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

# ==================== SESSION MANAGEMENT ====================
def init_session():
    if "last_temp" not in st.session_state:
        for k, v in MODERATE_PRESET.items():
            st.session_state[k] = v
    if "current_risk" not in st.session_state:
        st.session_state.current_risk = 1 # افتراضي
    if "patient_name" not in st.session_state:
        st.session_state.patient_name = "أحمد محمد"
        st.session_state.language = "ar"
        st.session_state.last_check = datetime.now() - timedelta(hours=2)
        st.session_state.device_battery = 87

def toggle_language():
    st.session_state.language = "en" if st.session_state.language == "ar" else "ar"
    st.rerun()

init_session()
lang = st.session_state.language

# ==================== LOAD MODEL ====================
@st.cache_resource
def get_model():
    return load_and_train_model()

model, base_model, metrics, feature_cols = get_model()

# ==================== HEADER & LOGO LOGIC ====================
# دالة مساعدة لتحويل الصورة إلى كود لعرضها والتحكم بها
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if os.path.exists("logo.png"):
        img_base64 = get_base64_image("logo.png")
        # إذا كان الخطر عالياً (2)، نضيف كلاس critical-logo للوميض
        logo_class = "critical-logo" if st.session_state.current_risk == 2 else ""
        
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{img_base64}" class="{logo_class}" width="150" style="border-radius: 50%;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("<div style='text-align: center; font-size: 60px;'>🧬</div>", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; margin-bottom: 10px;">
    <h1 style="margin:0;">{'مناعتي' if lang == 'ar' else 'Manaaty'}</h1>
    <p style="color: #8892b8;">{'نظام الحماية الذكي' if lang == 'ar' else 'Smart Protection System'}</p>
</div>
""", unsafe_allow_html=True)

if st.button("🌐 " + ("English" if lang == "ar" else "عربي"), key="lang_btn"):
    toggle_language()

# ==================== DEVICE INFO ====================
labels = {
    'battery': "البطارية" if lang == "ar" else "Battery",
    'next': "القراءة القادمة" if lang == "ar" else "Next Read",
    'status': "حالة الجهاز" if lang == "ar" else "Patch Status",
    'good': "جيدة" if lang == "ar" else "Good",
    'active': "نشط" if lang == "ar" else "Active",
    'auto': "تلقائي" if lang == "ar" else "Auto"
}

st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric(labels['battery'], f"{st.session_state.device_battery}%", labels['good'])
c2.metric(labels['next'], "2h", labels['auto'])
c3.metric(labels['status'], labels['active'], "OK")
st.markdown('</div>', unsafe_allow_html=True)

# ==================== SIMULATION CONTROLS ====================
st.markdown('<div class="mobile-card" style="border: 1px dashed #444;">', unsafe_allow_html=True)
st.caption("🛠️ " + ("اختبار سريع (تحديث الحالة فوراً):" if lang == "ar" else "Quick Test (Click to update status):"))
b1, b2, b3 = st.columns(3)

# عند الضغط: نحدث القيم + نحدث حالة الخطر في الذاكرة + Rerun
if b1.button("✅ " + ("طبيعي" if lang == "ar" else "Normal")):
    for k, v in LOW_PRESET.items(): st.session_state[k] = v
    st.session_state.current_risk = 0
    st.rerun()

if b2.button("⚠️ " + ("متوسط" if lang == "ar" else "Moderate")):
    for k, v in MODERATE_PRESET.items(): st.session_state[k] = v
    st.session_state.current_risk = 1
    st.rerun()

if b3.button("🚨 " + ("خطر" if lang == "ar" else "High")):
    for k, v in HIGH_PRESET.items(): st.session_state[k] = v
    st.session_state.current_risk = 2
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ==================== VITALS DISPLAY ====================
st.markdown(f"### {'مؤشراتك الحيوية' if lang == 'ar' else 'Current Vitals'}")

def get_css_class(val, low, high):
    if val < low or val > high: return "vital-row critical"
    if val < low*1.1 or val > high*0.9: return "vital-row elevated"
    return "vital-row"

vital_labels = {
    'Temp': 'الحرارة' if lang == 'ar' else 'Temp',
    'Heart': 'النبض' if lang == 'ar' else 'Heart Rate',
    'SpO2': 'الأكسجين' if lang == 'ar' else 'SpO2'
}

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
    lbl = vital_labels[label]
    st.markdown(f"""
    <div class="{css}">
        <div class="vital-label"><span>{icon}</span> {lbl}</div>
        <div class="vital-value">{val:.1f} <small>{unit}</small></div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==================== ANALYSIS LOGIC ====================
# زر التحليل اليدوي موجود هنا
if st.button("🔍 " + ("تحليل الحالة الآن" if lang == "ar" else "Analyze Health Status"), type="primary"):
    
    # 1. Prepare Data
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
        
        # تحديث حالة الجلسة للتأكد من تزامن اللوجو مع النتيجة
        if st.session_state.current_risk != pred_class:
            st.session_state.current_risk = pred_class
            st.rerun() # إعادة تحميل لتحديث وميض اللوجو فوراً

        # ================= 📳 VIBRATION =================
        if pred_class == 2:
            vibration_js = "<script>if(navigator.vibrate){navigator.vibrate([500, 200, 500]);}</script>"
            components.html(vibration_js, height=0, width=0)

        # 3. RESULT CARD
        card_class = "critical-alert-card" if pred_class == 2 else "mobile-card"
        
        st.markdown(f'<div class="{card_class}" style="text-align:center;">', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="status-badge {action['badge']}">
            {action['icon']} {action['title'] if lang == 'ar' else action['title_en']}
        </div>
        <h2 style="margin:10px 0;">{action['message'] if lang == 'ar' else action['message_en']}</h2>
        <p style="color:#667eea; font-weight:bold;">{('نسبة التأكد' if lang == 'ar' else 'Confidence')}: {pred_proba[pred_class]*100:.0f}%</p>
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
            base_vitals = {'temp': st.session_state.get('baseline_temp_c', 37), 'hr': st.session_state.get('baseline_hr_bpm', 70)}
            last_vitals = {'temp': st.session_state.get('last_temp', 37), 'hr': st.session_state.get('last_hr', 70)}
            st.plotly_chart(plot_vital_trends(base_vitals, last_vitals, pred_class), use_container_width=True)
            
            fig_shap, _ = plot_shap_analysis(base_model, input_df, pred_class, feature_cols)
            if fig_shap: st.plotly_chart(fig_shap, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
