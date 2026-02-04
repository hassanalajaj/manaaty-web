# pages/4_⚙️_Settings.py
import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

lang = st.session_state.get("language", "ar")

st.markdown(f'<h1 style="text-align:center; color: #1a7f8e; margin: 20px 0;">{"⚙️ الإعدادات" if lang == "ar" else "⚙️ Settings"}</h1>', unsafe_allow_html=True)

# Language
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f'<h3 class="card-title">{"اللغة" if lang == "ar" else "Language"}</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🇸🇦 العربية", use_container_width=True):
        st.session_state.language = "ar"
        st.rerun()
with col2:
    if st.button("🇬🇧 English", use_container_width=True):
        st.session_state.language = "en"
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Account
st.markdown('<div class="card">', unsafe_allow_html=True)
st.info(f"**ID:** {st.session_state.get('patient_id', 'N/A')}")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("🏠 " + ("الرئيسية" if lang == "ar" else "Home"), use_container_width=True):
    st.switch_page("pages/1_🏠_Home.py")

if st.button("🚪 " + ("خروج" if lang == "ar" else "Logout"), use_container_width=True):
    st.session_state.logged_in = False
    st.switch_page("app.py")

