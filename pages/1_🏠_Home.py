import streamlit as st
from config import CUSTOM_CSS, COLORS

st.set_page_config(page_title="Manaaty", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown(f"<h2 style='color:{COLORS['teal']};'>مرحباً، حسن العجاج 👋</h2>", unsafe_allow_html=True)

# المربعات الأربعة (Vitals, Risk, Trend, Biomarkers)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["red"]}; color:white;"><b>مستوى الخطر</b><br><h3>عالي ⚠️</h3></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["lavender"]};"><b>الاتجاه العام</b><br><h3>📈 متصاعد</h3></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["aqua"]};"><b>العلامات الحيوية</b><br><h3>37.8°C</h3></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["mint"]};"><b>المؤشرات</b><br><h3>CRP: 12.5</h3></div>', unsafe_allow_html=True)

# كرت التواصل
st.markdown(f'<div class="mobile-box" style="background:white; text-align:center;"><b>اتصل بالطبيب المباشر</b></div>', unsafe_allow_html=True)

# الصف السفلي: التوصية والملف الشخصي
c_recom, c_profile = st.columns(2)
with c_recom:
    st.markdown(f'<div class="mobile-box" style="background:white; border-left:6px solid {COLORS["aqua"]}; height:120px;"><b>📋 التوصية</b><br><small>يرجى الراحة التامة.</small></div>', unsafe_allow_html=True)
with c_profile:
    st.markdown(f'<div class="mobile-box" style="background:white; height:120px; text-align:right;"><b>👤 الملف الشخصي</b><br><b>حسن العجاج</b><br><small>ID: #29481 | O+</small></div>', unsafe_allow_html=True)
