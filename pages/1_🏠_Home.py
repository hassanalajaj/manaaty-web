import streamlit as st

try:
    from config import CUSTOM_CSS
except:
    CUSTOM_CSS = ""

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- تعريف الألوان المستوحاة من الصورة ---
# Teal: #1A5F7A | Light Blue: #D1E9F6 | Lavender: #D7D3F7 | Light Green: #B2E2D2
COLORS = {
    "teal": "#1A5F7A",
    "light_blue": "#D1E9F6",
    "lavender": "#D7D3F7",
    "light_green": "#B2E2D2",
    "white": "#FFFFFF",
    "text": "#2F3E46"
}

st.markdown(f"""
<style>
    /* تصميم الصندوق المربع الناعم */
    .mobile-box {{
        border-radius: 28px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 10px 25px rgba(0,0,0,0.02);
        margin-bottom: 15px;
        height: 150px;
        border: 1px solid rgba(255,255,255,0.5);
    }}
    
    .title-text {{ font-size: 14px; font-weight: 600; margin-bottom: 5px; opacity: 0.8; }}
    .value-text {{ font-size: 22px; font-weight: 800; }}
    .sub-text {{ font-size: 11px; opacity: 0.7; font-weight: 600; }}

    /* شريط البحث */
    .search-bar {{
        background: white;
        border-radius: 20px;
        padding: 12px 20px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        color: #90A4AE;
        display: flex;
        align-items: center;
    }}
</style>
""", unsafe_allow_html=True)

# --- المحتوى ---

# الترحيب باسم حسن
st.markdown(f"<h2 style='text-align: right; color: {COLORS['teal']};'>مرحباً، حسن 👋</h2>", unsafe_allow_html=True)

# شريط البحث
st.markdown('<div class="search-bar">🔍 بحث في سجلاتي...</div>', unsafe_allow_html=True)

# --- المنطق المنبثق للتوصيات (Pop-up) ---
if "toast_shown" not in st.session_state:
    st.toast("💡 توصية جديدة: يُفضل زيادة شرب الماء اليوم لضبط توازن الأملاح.", icon="✨")
    st.session_state.toast_shown = True

# --- شبكة المربعات (Grid) ---
col1, col2 = st.columns(2)

with col1:
    # 1. Risk Stratification (اللون التيل الغامق)
    st.markdown(f"""
    <div class="mobile-box" style="background-color: {COLORS['teal']}; color: white;">
        <div class="title-text">مستوى الخطر</div>
        <div class="value-text">High ⚠️</div>
        <div class="sub-text">Risk Stratification</div>
    </div>
    """, unsafe_allow_html=True)

    # 2. Trend (اللون البنفسجي اللافندر)
    st.markdown(f"""
    <div class="mobile-box" style="background-color: {COLORS['lavender']}; color: #4A44A4;">
        <div class="title-text">الاتجاه العام</div>
        <div class="value-text">📈 متصاعد</div>
        <div class="sub-text">Trend Analysis</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # 3. Vitals Data (اللون السماوي الفاتح)
    st.markdown(f"""
    <div class="mobile-box" style="background-color: {COLORS['light_blue']}; color: {COLORS['teal']};">
        <div class="title-text">العلامات الحيوية</div>
        <div class="value-text">37.8°C</div>
        <div class="sub-text">Baseline: 36.6° | Change: +1.2°</div>
    </div>
    """, unsafe_allow_html=True)

    # 4. Biomarkers (اللون الأخضر الفاتح)
    st.markdown(f"""
    <div class="mobile-box" style="background-color: {COLORS['light_green']}; color: #1E5642;">
        <div class="title-text">المؤشرات الحيوية</div>
        <div class="value-text">CRP: 12.5</div>
        <div class="sub-text">Baseline: 2.0 | Change: +10.5</div>
    </div>
    """, unsafe_allow_html=True)

# 5. Contact Physician (صندوق عريض)
st.markdown(f"""
<div class="mobile-box" style="background-color: #FFFFFF; height: 80px; flex-direction: row; align-items: center; border: 1px solid #E3F2FD;">
    <div style="font-size: 30px; margin-left: 20px;">👨‍⚕️</div>
    <div>
        <div style="font-weight: bold; color: {COLORS['teal']};">اتصل بالطبيب المباشر</div>
        <div style="font-size: 11px; opacity: 0.6;">Contact Physician (24/7)</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- الصف السفلي: التوصيات (يسار) والديموغرافيك (يمين) ---
c_left, c_right = st.columns(2)

with c_left:
    st.markdown(f"""
    <div class="mobile-box" style="background-color: #FFFFFF; height: 120px; border-left: 6px solid {COLORS['light_blue']};">
        <div style="color: {COLORS['teal']}; font-weight: bold; font-size: 13px;">📋 التوصية</div>
        <div style="font-size: 11px; margin-top: 10px; line-height: 1.4;">يرجى الالتزام بالراحة التامة وتجنب الإجهاد البدني لمدة 24 ساعة.</div>
    </div>
    """, unsafe_allow_html=True)

with c_right:
    st.markdown(f"""
    <div class="mobile-box" style="background-color: #FFFFFF; height: 120px; text-align: right;">
        <div class="title-text">👤 بيانات المريض</div>
        <div style="font-weight: 800; font-size: 16px;">حسن العكوز</div>
        <div style="font-size: 10px; opacity: 0.6; margin-top: 5px;">
            العمر: 30 سنة<br>فصيلة الدم: O+<br>ID: #29481
        </div>
    </div>
    """, unsafe_allow_html=True)

# شريط التنقل السفلي (Bottom Nav)
st.markdown(f"""
<div style="position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); 
            background: white; padding: 10px 50px; border-radius: 40px; 
            box-shadow: 0 10px 40px rgba(0,0,0,0.08); display: flex; gap: 50px; z-index: 1000;">
    <div style="font-size: 22px; opacity: 0.2;">👤</div>
    <div style="font-size: 24px; color: {COLORS['teal']}; transform: scale(1.2);">🏠</div>
    <div style="font-size: 22px; opacity: 0.2;">⚙️</div>
</div>
""", unsafe_allow_html=True)
