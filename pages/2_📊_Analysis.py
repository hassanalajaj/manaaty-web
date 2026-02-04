# pages/2_📊_Analysis.py
import streamlit as st
from config import CUSTOM_CSS, LOW_PRESET, MID_PRESET, HIGH_PRESET, RISK_LEVELS

st.set_page_config(page_title="Analysis", page_icon="📊", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

lang = st.session_state.get("language", "ar")

if "baseline_temp_c" not in st.session_state:
    for k, v in LOW_PRESET.items():
        st.session_state[k] = v

st.markdown(f'<h1 style="text-align:center; color: #1a7f8e; margin: 20px 0;">{"📊 تحليل الحالة" if lang == "ar" else "📊 Analysis"}</h1>', unsafe_allow_html=True)

# Quick Test
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✅ Low", use_container_width=True):
        for k, v in LOW_PRESET.items():
            st.session_state[k] = v
        st.rerun()

with col2:
    if st.button("⚠️ Mid", use_container_width=True):
        for k, v in MID_PRESET.items():
            st.session_state[k] = v
        st.rerun()

with col3:
    if st.button("🚨 High", use_container_width=True):
        for k, v in HIGH_PRESET.items():
            st.session_state[k] = v
        st.rerun()

# Vitals
st.markdown(f"""
<div class="card">
<h3 class="card-title">{"المؤشرات" if lang == "ar" else "Vitals"}</h3>
<div class="vital-grid">
    <div class="vital-box">
        <div class="vital-icon">🌡️</div>
        <div class="vital-value">{st.session_state.last_temp:.1f}°</div>
    </div>
    <div class="vital-box">
        <div class="vital-icon">💓</div>
        <div class="vital-value">{st.session_state.last_hr}</div>
    </div>
    <div class="vital-box">
        <div class="vital-icon">🫁</div>
        <div class="vital-value">{st.session_state.last_spo2:.0f}%</div>
    </div>
    <div class="vital-box">
        <div class="vital-icon">🔬</div>
        <div class="vital-value">{st.session_state.baseline_crp_mg_l:.1f}</div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# Analyze
if st.button("🔍 " + ("تحليل" if lang == "ar" else "Analyze"), type="primary", use_container_width=True):
    temp = st.session_state.last_temp
    hr = st.session_state.last_hr
    crp = st.session_state.baseline_crp_mg_l
    
    if temp > 38.0 or hr > 110 or crp > 10:
        risk_level = 2
    elif temp > 37.5 or hr > 90 or crp > 2:
        risk_level = 1
    else:
        risk_level = 0
    
    risk = RISK_LEVELS[risk_level]
    
    st.markdown(f"""
    <div class="status-card status-{risk['color']}">
        <div class="status-icon">{risk['icon']}</div>
        <div class="status-title">{risk['name_ar'] if lang == 'ar' else risk['name_en']}</div>
        <div class="status-message">{risk['message_ar'] if lang == 'ar' else risk['message_en']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    if risk_level == 2:
        if st.button("🚨 " + ("اتصل بالإسعاف 997" if lang == "ar" else "Call 997"), type="primary", use_container_width=True):
            st.balloons()
            st.success("🚑 " + ("تم الاتصال" if lang == "ar" else "Called"))

if st.button("🏠 " + ("الرئيسية" if lang == "ar" else "Home"), use_container_width=True):
    st.switch_page("pages/1_🏠_Home.py")

