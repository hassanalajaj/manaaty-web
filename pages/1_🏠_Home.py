import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ألوان الباستيل من صورك
C_TEAL = "#1A5F7A"
C_LAVENDER = "#D7D3F7"
C_AQUA = "#D1E9F6"
C_MINT = "#B2E2D2"

st.markdown(f"<h2 style='text-align: right; color: {C_TEAL};'>مرحباً، حسن العجاج 👋</h2>", unsafe_allow_html=True)

# المربعات الرئيسية
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="mobile-box" style="background:{C_TEAL}; color:white;"><b>مستوى الخطر</b><br><small>Risk Stratification</small><h3>عالي ⚠️</h3></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mobile-box" style="background:{C_LAVENDER}; color:#4A44A4;"><b>الاتجاه العام</b><br><small>Trend Analysis</small><h3>📈 متصاعد</h3></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="mobile-box" style="background:{C_AQUA}; color:{C_TEAL};"><b>العلامات الحيوية</b><br><small>Vitals Data</small><h3>37.8°C</h3></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mobile-box" style="background:{C_MINT}; color:#1E5642;"><b>المؤشرات</b><br><small>Biomarker Data</small><h3>CRP: 12.5</h3></div>', unsafe_allow_html=True)

# صندوق التواصل
st.markdown(f'<div class="mobile-box" style="background:white; display:flex; align-items:center; gap:15px; height:80px; border:1px solid #eee;"> <span style="font-size:30px;">👨‍⚕️</span> <div><b>اتصل بالطبيب المباشر</b><br><small>Contact Physician</small></div></div>', unsafe_allow_html=True)

# الصف السفلي: التوصية والملف الشخصي
c_left, c_right = st.columns(2)
with c_left:
    st.markdown(f'<div class="mobile-box" style="background:white; height:120px; border-left:6px solid {C_AQUA};"><b>📋 التوصية</b><br><p style="font-size:11px; margin-top:5px;">يرجى الالتزام بالراحة التامة وتناول السوائل بانتظام.</p></div>', unsafe_allow_html=True)

with c_right:
    # تم تعديل الاسم هنا بناءً على طلبك
    st.markdown(f'<div class="mobile-box" style="background:white; height:120px; text-align:right;"><b>👤 الملف الشخصي</b><br><b style="font-size:16px;">حسن العجاج</b><br><small>ID: #29481 | O+</small></div>', unsafe_allow_html=True)

# شريط التنقل السفلي - نسخة "هادئة" جداً (Minimalist)
st.markdown(f"""
<div class="nav-bar">
    <div style="font-size: 20px; opacity: 0.2;">👤</div>
    <div style="font-size: 24px; color: {C_TEAL};">🏠</div>
    <div style="font-size: 20px; opacity: 0.2;">⚙️</div>
</div>
""", unsafe_allow_html=True)
