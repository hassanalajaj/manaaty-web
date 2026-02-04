import streamlit as st
import pandas as pd
import numpy as np

# محاولة استدعاء التصميم العام
try:
    from config import CUSTOM_CSS
except:
    CUSTOM_CSS = ""

st.set_page_config(page_title="Manaaty Dashboard", page_icon="🧬", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- تنسيقات CSS مخصصة لتحقيق شكل الجوال والألوان المريحة ---
st.markdown("""
<style>
    .block-container { padding-top: 2rem !important; }
    
    /* الحاوية الأساسية للمربعات */
    .grid-wrapper {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-bottom: 15px;
    }

    /* تصميم المربع (Box) */
    .status-box {
        border-radius: 24px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        border: 1px solid rgba(255,255,255,0.3);
    }

    /* الألوان المريحة (Pastel Palette) */
    .bg-teal { background-color: #0E5159; color: white; } /* غامق للتميز */
    .bg-lavender { background-color: #E8EAF6; color: #3949AB; } /* بنفسجي هادئ */
    .bg-blue { background-color: #DCEAF2; color: #0E5159; } /* سماوي فاتح */
    .bg-green { background-color: #E0F2F1; color: #00695C; } /* أخضر نعناعي */
    .bg-white { background-color: #FFFFFF; color: #2F3E46; border: 1px solid #ECEFF1; }

    .box-title { font-size: 14px; font-weight: 700; opacity: 0.9; margin-bottom: 8px; }
    .box-value { font-size: 20px; font-weight: 800; }
    .box-delta { font-size: 12px; font-weight: 600; margin-top: 4px; }
    
    /* التوصية المنبثقة أسفل اليسار والديموغرافيك أسفل اليمين */
    .footer-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- منطق التوصية المنبثقة (Pop-up) ---
if "recom_shown" not in st.session_state:
    st.toast("💡 توصية: يرجى زيادة شرب السوائل ومراقبة الحرارة كل 4 ساعات.", icon="ℹ️")
    st.session_state.recom_shown = True

# --- المحتوى الرئيسي ---

st.markdown(f"<h3 style='text-align: right; color: #0E5159;'>مرحباً، {st.session_state.get('patient_id', 'عبير')} 👋</h3>", unsafe_allow_html=True)

# 1. Risk Stratification (Box - Top Full Width)
st.markdown("""
<div class="status-box bg-teal" style="margin-bottom:15px; height: 100px; justify-content: center; align-items: center;">
    <div class="box-title">تصنيف المخاطر (Risk Stratification)</div>
    <div class="box-value" style="font-size: 28px;">⚠️ مستوى مرتفع (High)</div>
</div>
""", unsafe_allow_html=True)

# 2. Grid for Vitals, Biomarkers, Trend, and Contact
col1, col2 = st.columns(2)

with col1:
    # Vitals Data
    st.markdown("""
    <div class="status-box bg-lavender" style="height: 140px;">
        <div class="box-title">العلامات الحيوية (Vitals)</div>
        <div class="box-value">37.8°C</div>
        <div class="box-delta">الأساس: 36.6° | التغيير: +1.2° 🔺</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Trend Box
    st.markdown("""
    <div class="status-box bg-white" style="height: 140px; border: 1px solid #D1E3E7;">
        <div class="box-title">الاتجاه العام (Trend)</div>
        <div style="font-size: 30px; text-align: center; margin-top: 10px;">📈</div>
        <div class="box-delta" style="text-align:center;">ارتفاع تدريجي في الالتهاب</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Biomarker Data
    st.markdown("""
    <div class="status-box bg-green" style="height: 140px;">
        <div class="box-title">المؤشرات (Biomarkers)</div>
        <div class="box-value">CRP: 12.5</div>
        <div class="box-delta">الأساس: 2.0 | التغيير: +10.5 🔺</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Physician
    st.markdown("""
    <div class="status-box bg-blue" style="height: 140px; cursor: pointer;">
        <div class="box-title">اتصل بالطبيب</div>
        <div style="font-size: 30px; text-align: center; margin-top: 10px;">📞</div>
        <div class="box-delta" style="text-align:center;">تواصل فوري (24/7)</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Bottom Row: Recommendations (Left) & Demographics (Right)
st.markdown("<div class='footer-grid'>", unsafe_allow_html=True)
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div class="status-box bg-white" style="height: 120px; border-left: 5px solid #42A5F5;">
        <div class="box-title" style="color:#1E88E5;">📋 التوصية</div>
        <div style="font-size: 12px; line-height: 1.4;">يرجى الالتزام بالراحة التامة وتجنب الأماكن المزدحمة حالياً.</div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown(f"""
    <div class="status-box bg-white" style="height: 120px; text-align: right;">
        <div class="box-title">👤 بيانات المريض</div>
        <div style="font-size: 13px; font-weight: bold;">{st.session_state.get('patient_id', 'عبير العكوز')}</div>
        <div style="font-size: 11px; opacity: 0.7;">العمر: 28 سنة | فصيلة الدم: O+</div>
        <div style="font-size: 10px; margin-top: 5px;">ID: #992834</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# شريط التنقل السفلي الوهمي
st.markdown("""
<div style="position: fixed; bottom: 15px; left: 50%; transform: translateX(-50%); 
            background: white; padding: 10px 40px; border-radius: 40px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); display: flex; gap: 50px; z-index: 1000;">
    <div style="font-size: 20px; opacity: 0.3;">👤</div>
    <div style="font-size: 24px; color: #0E5159;">🏠</div>
    <div style="font-size: 20px; opacity: 0.3;">⚙️</div>
</div>
""", unsafe_allow_html=True)
