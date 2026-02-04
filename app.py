import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(
    page_title="Manaaty",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.language = "ar"

if st.session_state.logged_in:
    st.switch_page("pages/1_🏠_Home.py")

lang = st.session_state.language

# --- قسم الهيدر (الشعار) بتصميم المنحنى الجديد ---
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.markdown('<div style="font-size:60px; margin-bottom:10px;">🧬</div>', unsafe_allow_html=True)
st.markdown(f'<h1 class="app-title">{"مناعتي" if lang == "ar" else "Manaaty"}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="app-subtitle">{"رعايـة ذكيـة .. لحياة آمنـة" if lang == "ar" else "Smart Care for a Safe Life"}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- كارد تسجيل الدخول (زجاجي) ---
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(f'<h3 style="text-align:center; margin-bottom: 20px; color:#4FA6B3;">{"أهلاً بك مجدداً" if lang == "ar" else "Welcome Back"}</h3>', unsafe_allow_html=True)

# حقول الإدخال
patient_id = st.text_input("🆔", placeholder=("رقم الملف الطبي" if lang == "ar" else "Medical File ID"))
password = st.text_input("🔒", placeholder=("كلمة المرور" if lang == "ar" else "Password"), type="password")

st.markdown("<br>", unsafe_allow_html=True)

# زر الدخول الكبير
if st.button(("تسجيل الدخول" if lang == "ar" else "Login"), type="primary", use_container_width=True):
    if patient_id and password:
        st.session_state.patient_id = patient_id
        st.session_state.logged_in = True
        st.switch_page("pages/1_🏠_Home.py")
    else:
        st.toast("⚠️ " + ("البيانات غير مكتملة" if lang == "ar" else "Missing credentials"))

# خيارات إضافية (اللغة والديمو)
st.markdown("<br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    if st.button("English / عربي"):
        st.session_state.language = "en" if lang == "ar" else "ar"
        st.rerun()
with c2:
    if st.button("تجربة (Demo)"):
        st.session_state.patient_id = "Demo-User"
        st.session_state.logged_in = True
        st.switch_page("pages/1_🏠_Home.py")

st.markdown('</div>', unsafe_allow_html=True)

# تذييل بسيط
st.markdown(f"""
<div style="text-align: center; margin-top: 30px; opacity: 0.6;">
    <p style="font-size: 12px;">© 2024 Manaaty Health System</p>
</div>
""", unsafe_allow_html=True)
