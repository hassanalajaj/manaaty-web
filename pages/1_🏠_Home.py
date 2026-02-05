import streamlit as st
from config import CUSTOM_CSS, COLORS

st.set_page_config(page_title="Manaaty Dashboard", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# الترحيب العلوي
st.markdown(f"<h2 style='color:{COLORS['teal']};'>مرحباً، حسن العجاج 👋</h2>", unsafe_allow_html=True)

# شبكة البيانات (الخطر، العلامات، الاتجاه، المؤشرات)
col1, col2 = st.columns(2)
with col1:
    # كرت الخطر (أحمر)
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["red"]}; color:white;"><b>مستوى الخطر</b><br><h3 style="color:white;">عالي ⚠️</h3></div>', unsafe_allow_html=True)
    # كرت الاتجاه العام (لافندر)
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["lavender"]};"><b>الاتجاه العام</b><br><h3>📈 متصاعد</h3></div>', unsafe_allow_html=True)
with col2:
    # كرت العلامات الحيوية (سماوي)
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["aqua"]};"><b>العلامات الحيوية</b><br><h3>37.8°C</h3></div>', unsafe_allow_html=True)
    # كرت المؤشرات (مينت)
    st.markdown(f'<div class="mobile-box" style="background:{COLORS["mint"]};"><b>المؤشرات</b><br><h3>CRP: 12.5</h3></div>', unsafe_allow_html=True)

# كرت التواصل (أبيض مع نص أسود)
st.markdown(f'<div class="mobile-box" style="background:white; text-align:center;"><b>اتصل بالطبيب المباشر</b><br><small>Contact Physician</small></div>', unsafe_allow_html=True)

# الصف السفلي: التوصية والملف الشخصي
c_recom, c_profile = st.columns(2)
with c_recom:
    # التوصية (يسار)
    st.markdown(f'<div class="mobile-box" style="background:white; border-left:6px solid {COLORS["aqua"]}; height:130px;"><b>📋 التوصية</b><br><p style="font-size:12px;">يرجى الالتزام بالراحة التامة وتناول السوائل.</p></div>', unsafe_allow_html=True)
with c_profile:
    # الملف الشخصي (يمين) - توضيح الاسم بالأسود بناءً على طلبك
    st.markdown(f"""
    <div class="mobile-box" style="background:white; height:130px; text-align:right;">
        <b>👤 الملف الشخصي</b><br>
        <b style="font-size:18px; color:{COLORS['black']};">حسن العجاج</b><br>
        <small style="color:#666;">ID: #29481 | فصيلة الدم: O+</small>
    </div>
    """, unsafe_allow_html=True)

# شريط التنقل السفلي الهادئ
st.markdown(f"""
<div class="nav-bar">
    <div style="font-size: 20px; opacity: 0.2;">👤</div>
    <div style="font-size: 24px; color: {COLORS['teal']};">🏠</div>
    <div style="font-size: 20px; opacity: 0.2;">⚙️</div>
</div>
""", unsafe_allow_html=True)
