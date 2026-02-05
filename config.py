import streamlit as st

# ألوان التصميم المستخرجة من Figma
COLORS = {
    "teal": "#1A5F7A",
    "aqua": "#D1E9F6",
    "lavender": "#D7D3F7",
    "mint": "#B2E2D2",
    "red": "#E53935",
    "black": "#000000"
}

CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
* {{ font-family: 'Cairo', sans-serif; direction: rtl; color: {COLORS['black']}; }}
.stApp {{ background: linear-gradient(180deg, #FFFFFF 0%, #F0F7F9 100%); }}
#MainMenu, footer, header {{visibility: hidden;}}

.mobile-box {{
    border-radius: 28px;
    padding: 20px;
    margin-bottom: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.02);
    border: 1px solid rgba(0,0,0,0.05);
}}
</style>
"""

# البيانات لضمان عدم حدوث ImportError
LOW_PRESET = {"last_temp": 36.6, "last_hr": 72, "last_spo2": 98, "baseline_crp_mg_l": 2.0}
MID_PRESET = {"last_temp": 37.5, "last_hr": 92, "last_spo2": 95, "baseline_crp_mg_l": 8.0}
HIGH_PRESET = {"last_temp": 38.8, "last_hr": 115, "last_spo2": 91, "baseline_crp_mg_l": 15.0}
RISK_LEVELS = {{ 0: 'مستقر', 1: 'تنبيه', 2: 'خطر عالي' }}
