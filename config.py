import streamlit as st

# 1. التصميم البصري (CSS) - ألوان هادئة وواجهة جوال نظيفة
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

* { font-family: 'Cairo', sans-serif; direction: rtl; }

.stApp {
    background: linear-gradient(180deg, #FFFFFF 0%, #F4F9FA 100%);
    background-attachment: fixed;
}

#MainMenu, footer, header {visibility: hidden;}

/* كرت المعلومات (Soft UI) */
.mobile-box {
    border-radius: 30px;
    padding: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.02);
    border: 1px solid rgba(255,255,255,0.7);
    margin-bottom: 12px;
}

/* شريط التنقل السفلي - تصميم بسيط وغير مزعج */
.nav-bar {
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
    border: 1px solid #E0E0E0;
}
</style>
"""

# 2. البيانات التي تحتاجها صفحة التحليل (لحل الـ ImportError)
LOW_PRESET = {"last_temp": 36.6, "last_hr": 72, "last_spo2": 98, "baseline_crp_mg_l": 2.0}
MID_PRESET = {"last_temp": 37.5, "last_hr": 92, "last_spo2": 95, "baseline_crp_mg_l": 8.0}
HIGH_PRESET = {"last_temp": 38.8, "last_hr": 115, "last_spo2": 91, "baseline_crp_mg_l": 15.0}

RISK_LEVELS = {
    0: {'name_ar': 'مستقر', 'color': '#B2E2D2', 'icon': '✅'},
    1: {'name_ar': 'تنبيه', 'color': '#D7D3F7', 'icon': '⚠️'},
    2: {'name_ar': 'خطر', 'color': '#1A5F7A', 'icon': '🚨'}
}
