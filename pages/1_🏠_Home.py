# pages/1_🏠_Home.py
import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

lang = st.session_state.get("language", "ar")

st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.markdown('<div style="font-size:70px;">🧬</div>', unsafe_allow_html=True)
st.markdown(f'<h1 class="app-title">{"مرحباً" if lang == "ar" else "Welcome"}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="app-subtitle">{st.session_state.get("patient_id", "Guest")}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Device Status
st.markdown(f"""
<div class="device-bar">
    <div class="device-item">
        <div class="device-icon">🔋</div>
        <div class="device-value">87%</div>
    </div>
    <div class="device-item">
        <div class="device-icon">📅</div>
        <div class="device-value">4{"د" if lang == "ar" else "d"}</div>
    </div>
    <div class="device-item">
        <div class="device-icon">⏱️</div>
        <div class="device-value">2{"س" if lang == "ar" else "h"}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Menu
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊\n" + ("تحليل" if lang == "ar" else "Analysis"), use_container_width=True):
        st.switch_page("pages/2_📊_Analysis.py")

with col2:
    if st.button("📈\n" + ("السجل" if lang == "ar" else "History"), use_container_width=True):
        st.switch_page("pages/3_📈_History.py")

with col3:
    if st.button("⚙️\n" + ("إعدادات" if lang == "ar" else "Settings"), use_container_width=True):
        st.switch_page("pages/4_⚙️_Settings.py")

# Current Status
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f'<h3 class="card-title">{"حالتك الحالية" if lang == "ar" else "Current Status"}</h3>', unsafe_allow_html=True)

st.markdown("""
<div class="vital-grid">
    <div class="vital-box">
        <div class="vital-icon">🌡️</div>
        <div class="vital-value">36.7°</div>
    </div>
    <div class="vital-box">
        <div class="vital-icon">💓</div>
        <div class="vital-value">72</div>
    </div>
    <div class="vital-box">
        <div class="vital-icon">🫁</div>
        <div class="vital-value">98%</div>
    </div>
    <div class="vital-box">
        <div class="vital-icon">🔬</div>
        <div class="vital-value">0.5</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚪 " + ("تسجيل الخروج" if lang == "ar" else "Logout"), use_container_width=True):
    st.session_state.logged_in = False
    st.switch_page("app.py")

