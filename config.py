import streamlit as st

# 1. التصميم البصري (CSS)
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

* { font-family: 'Cairo', sans-serif; direction: rtl; }

.stApp {
    background: linear-gradient(180deg, #FFFFFF 0%, #F4F9FA 100%);
    background-attachment: fixed;
}

#MainMenu, footer, header {visibility: hidden;}

/* كرت المعلومات */
.mobile-box {
    border-radius: 25px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    margin-bottom: 12px;
    border: 1px solid rgba(0,0,0,0.05);
}

/* نمط النص الأسود الواضح للكروت البيضاء */
.dark-text {
    color: #000000 !important;
}

.sub-text-dark {
    color: #424242 !important;
    font-size: 11px;
}

/* شريط التنقل */
.nav-bar {
    position: fixed;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    background: white;
    padding: 10px 40px;
    border-radius: 40px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    display: flex;
    gap: 50px;
    z-index: 1000;
}
</style>
"""

# 2. إضافة البيانات المفقودة (لحل خطأ ImportError)
LOW_PRESET = {"last_temp": 36.6, "last_hr": 72, "last_spo2": 98, "baseline_crp_mg_l": 2.0}
MID_PRESET = {"last_temp": 37.5, "last_hr": 92, "last_spo2": 95, "baseline_crp_mg_l": 8.0}
HIGH_PRESET = {"last_temp": 38.8, "last_hr": 115, "last_spo2": 91, "baseline_crp_mg_l": 15.0}

RISK_LEVELS = {
    0: {'name_ar': 'مستقر', 'color': '#B2E2D2', 'icon': '✅'},
    1: {'name_ar': 'تنبيه', 'color': '#D7D3F7', 'icon': '⚠️'},
    2: {'name_ar': 'خطر', 'color': '#1A5F7A', 'icon': '🚨'}
}
