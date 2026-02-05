import streamlit as st

# تعريف الألوان الأساسية كما في الصورة (ألوان باستيل هادئة)
COLORS = {
    "teal": "#1A5F7A",    # اللون الرئيسي
    "aqua": "#D1E9F6",    # سماوي فاتح
    "lavender": "#D7D3F7", # بنفسجي هادئ
    "mint": "#B2E2D2",     # أخضر فاتح
    "red": "#E53935",      # أحمر للخطر
    "black": "#000000",    # أسود صريح للنصوص
    "white": "#FFFFFF"     # أبيض للكروت
}

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

/* الخط العام واللون الأسود الأساسي للنصوص */
* {{ 
    font-family: 'Cairo', sans-serif; 
    direction: rtl; 
    color: {COLORS['black']}; 
}}

/* خلفية التطبيق المتدرجة */
.stApp {{ 
    background: linear-gradient(180deg, #FFFFFF 0%, #F0F7F9 100%); 
    background-attachment: fixed;
}}

/* إخفاء القوائم غير الضرورية لتقليل القلق البصري */
#MainMenu, footer, header {{ visibility: hidden; }}

/* تصميم الكروت (Soft UI) بزوايا دائرية جداً */
.mobile-box {{
    border-radius: 28px;
    padding: 20px;
    margin-bottom: 12px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.02);
    border: 1px solid rgba(0,0,0,0.05);
}}

/* شريط التنقل السفلي */
.nav-bar {{
    position: fixed;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    padding: 10px 40px;
    border-radius: 40px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    display: flex;
    gap: 50px;
    z-index: 1000;
}}
</style>
"""

# متغيرات لصفحة التحليل لمنع الأخطاء المستقبيلة
LOW_PRESET = {"last_temp": 36.6, "last_hr": 72, "last_spo2": 98, "baseline_crp_mg_l": 2.0}
MID_PRESET = {"last_temp": 37.5, "last_hr": 92, "last_spo2": 95, "baseline_crp_mg_l": 8.0}
HIGH_PRESET = {"last_temp": 38.8, "last_hr": 115, "last_spo2": 91, "baseline_crp_mg_l": 15.0}
RISK_LEVELS = { 0: 'مستقر', 1: 'تنبيه', 2: 'خطر عالي' }
