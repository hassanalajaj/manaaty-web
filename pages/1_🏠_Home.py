import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ألوان الكروت المريحة
C_LAVENDER = "#D7D3F7"
C_AQUA = "#D1E9F6"
C_MINT = "#B2E2D2"

st.markdown(f"<h2 style='text-align: right; color: #1A5F7A;'>مرحباً، حسن العجاج 👋</h2>", unsafe_allow_html=True)

# --- الصف الأول ---
col1, col2 = st.columns(2)
with col1:
    # كرت العلامات الحيوية
    st.markdown(f'<div class="mobile-box" style="background:{C_AQUA}; color:#1A5F7A;"><b>العلامات الحيوية</b><br><small>Vitals Data</small><h3>37.8°C</h3></div>', unsafe_allow_html=True)

with col2:
    # كرت مستوى الخطر (تم تغييره للأحمر كما طلبت)
    st.markdown(f'<div class="mobile-box bg-danger"><b>مستوى الخطر</b><br><small>Risk Stratification</small><h3>عالي ⚠️</h3></div>', unsafe_allow_html=True)

# --- الصف الثاني ---
col3, col4 = st.columns(2)
with col3:
    # كرت المؤشرات
    st.markdown(f'<div class="mobile-box" style="background:{C_MINT}; color:#1E5642;"><b>المؤشرات</b><br><small>Biomarker Data</small><h3>CRP: 12.5</h3></div>', unsafe_allow_html=True)

with col4:
    # كرت الاتجاه العام
    st.markdown(f'<div class="mobile-box" style="background:{C_LAVENDER}; color:#4A44A4;"><b>الاتجاه العام</b><br><small>Trend Analysis</small><h3>متصاعد 📈</h3></div>', unsafe_allow_html=True)

# --- كرت الاتصال بالطبيب (نص أسود واضح) ---
st.markdown(f'<div class="mobile-box" style="background:white; text-align:center; border:1px solid #E0E0E0;"><b class="text-black">اتصل بالطبيب المباشر</b><br><small class="text-black-small">Contact Physician</small></div>', unsafe_allow_html=True)

# --- الصف السفلي (الاسم والتوصية) ---
c_left, c_right = st.columns(2)
with c_left:
    # الملف الشخصي (حسن العجاج بالأسود)
    st.markdown(f"""
    <div class="mobile-box" style="background:white; height:130px; text-align:right; border:1px solid #E0E0E0;">
        <b class="text-black">👤 الملف الشخصي</b><br>
        <b class="text-black" style="font-size:18px;">حسن العجاج</b><br>
        <small class="text-black-small">ID: #29481 | فصيلة الدم: O+</small>
    </div>
    """, unsafe_allow_html=True)

with c_right:
    # التوصية (نص أسود واضح)
    st.markdown(f"""
    <div class="mobile-box" style="background:white; height:130px; border-left:6px solid {C_AQUA}; border-top:1px solid #E0E0E0; border-right:1px solid #E0E0E0; border-bottom:1px solid #E0E0E0;">
        <b class="text-black">📋 التوصية</b><br>
        <p class="text-black-small">يرجى الالتزام بالراحة التامة وتناول السوائل بانتظام ومراقبة درجة الحرارة.</p>
    </div>
    """, unsafe_allow_html=True)

# شريط التنقل السفلي الهادئ
st.markdown(f"""
<div class="nav-bar">
    <div style="font-size: 20px; opacity: 0.2;">👤</div>
    <div style="font-size: 24px; color: #1A5F7A;">🏠</div>
    <div style="font-size: 20px; opacity: 0.2;">⚙️</div>
</div>
""", unsafe_allow_html=True)
