# app.py
import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(
    page_title="Manaaty | مناعتي",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.language = "ar"

# Don't auto-redirect - let user navigate naturally
lang = st.session_state.language

# Logo
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.markdown('<div style="font-size:80px; text-align:center;">🧬</div>', unsafe_allow_html=True)
st.markdown(f'<h1 class="app-title">{"مناعتي" if lang == "ar" else "Manaaty"}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="app-subtitle">{"نظام الكشف المبكر عن العدوى" if lang == "ar" else "Early Infection Detection System"}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Check if already logged in - show message instead of redirect
if st.session_state.logged_in:
    st.success("✅ " + ("أنت مسجل دخول بالفعل" if lang == "ar" else "Already logged in"))
    if st.button("🏠 " + ("انتقل للرئيسية" if lang == "ar" else "Go to Home"), type="primary", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")
    st.stop()

# Login Form
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f'<h2 class="card-title">{"تسجيل الدخول" if lang == "ar" else "Login"}</h2>', unsafe_allow_html=True)

patient_id = st.text_input("🆔 " + ("رقم المريض" if lang == "ar" else "Patient ID"), placeholder="P-12345")
password = st.text_input("🔒 " + ("كلمة المرور" if lang == "ar" else "Password"), type="password")

col1, col2 = st.columns(2)
with col1:
    if st.button("🌐 " + ("EN" if lang == "ar" else "AR"), use_container_width=True):
        st.session_state.language = "en" if lang == "ar" else "ar"
        st.rerun()

with col2:
    if st.button("🔍 Demo", use_container_width=True):
        st.session_state.patient_id = "P-DEMO"
        st.session_state.logged_in = True
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

if st.button("➡️ " + ("دخول" if lang == "ar" else "Login"), type="primary", use_container_width=True):
    if patient_id and password:
        st.session_state.patient_id = patient_id
        st.session_state.logged_in = True
        st.rerun()
    else:
        st.error("❌ " + ("يرجى إدخال البيانات" if lang == "ar" else "Please enter credentials"))

# Show navigation button if logged in
if st.session_state.logged_in:
    if st.button("🏠 " + ("انتقل للرئيسية" if lang == "ar" else "Go to Home"), use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

st.markdown(f"""
<div style="text-align: center; margin-top: 40px; color: #546e7a; font-size: 12px;">
    <p>{"جامعة الملك سعود للعلوم الصحية" if lang == "ar" else "King Saud University for Health Sciences"}</p>
</div>
""", unsafe_allow_html=True)
