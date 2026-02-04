
# pages/3_📈_History.py
import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(page_title="History", page_icon="📈", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

lang = st.session_state.get("language", "ar")

st.markdown(f'<h1 style="text-align:center; color: #1a7f8e; margin: 20px 0;">{"📈 السجل" if lang == "ar" else "📈 History"}</h1>', unsafe_allow_html=True)

st.info("📊 " + ("سجل القراءات السابقة" if lang == "ar" else "Previous readings history"))

if st.button("🏠 " + ("الرئيسية" if lang == "ar" else "Home"), use_container_width=True):
    st.switch_page("pages/1_🏠_Home.py")
