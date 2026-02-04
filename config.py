import streamlit as st

# 1. تصميم الواجهة (CSS) بناءً على الـ Design System الجديد
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

/* --- Global Settings --- */
* {
    font-family: 'Cairo', sans-serif;
    color: #2F3E46; /* Primary Text: Dark Desaturated Blue-Gray */
}

/* --- Background Gradient (Top -> Bottom) --- */
/* Top: #FFFFFF, Middle: #F1F8F9, Bottom: #E3F0F2 */
.stApp {
    background: linear-gradient(180deg, #FFFFFF 0%, #F1F8F9 50%, #E3F0F2 100%);
    background-attachment: fixed;
}

/* --- Typography --- */
h1, h2, h3 {
    color: #4FA6B3 !important; /* Primary Teal */
    font-weight: 700;
}

p, label, .stMarkdown {
    color: #6B7C85; /* Secondary Text: Muted Gray-Blue */
}

/* --- Containers & Cards (Glass-morphism) --- */
/* White with 80-95% opacity, soft shadow, rounded corners */
.card, .stForm, div[data-testid="stVerticalBlock"] > div {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid #DCE8EA; /* Almost invisible border */
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0px 8px 24px rgba(79, 166, 179, 0.12); /* Soft Medical Shadow */
    backdrop-filter: blur(10px);
}

/* --- Logo Container --- */
.logo-container {
    text-align: center;
    padding: 40px 20px;
    /* Gradient: Left #6FBFC7 -> Right #4FA6B3 */
    background: linear-gradient(135deg, #6FBFC7 0%, #4FA6B3 100%);
    margin: -1rem -1rem 30px -1rem;
    border-radius: 0 0 40px 40px;
    box-shadow: 0px 10px 30px rgba(79, 166, 179, 0.2);
}

.app-title {
    color: white !important;
    font-size: 36px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.app-subtitle {
    color: rgba(255,255,255,0.95) !important;
    font-size: 16px;
    font-weight: 300;
}

/* --- Buttons (Primary Action) --- */
.stButton > button {
    width: 100%;
    /* Gradient: Left #6FBFC7 -> Right #4FA6B3 */
    background: linear-gradient(135deg, #6FBFC7 0%, #4FA6B3 100%);
    color: white !important;
    border: none;
    border-radius: 16px;
    padding: 16px;
    font-size: 18px;
    font-weight: 600;
    box-shadow: 0 8px 20px rgba(79, 166, 179, 0.25);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(79, 166, 179, 0.35);
}

/* --- Inputs --- */
.stTextInput > div > div > input {
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid #DCE8EA;
    border-radius: 12px;
    color: #2F3E46;
    height: 50px;
}

.stTextInput > div > div > input:focus {
    border-color: #4FA6B3;
    box-shadow: 0 0 0 2px rgba(79, 166, 179, 0.2);
}

/* --- Status Cards --- */
.status-card {
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    margin: 20px 0;
    border: 1px solid;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

/* Success: #7ED1C2 */
.status-low {
    background: #F4FAFB; 
    border-color: #7ED1C2;
}
.status-low .status-icon { color: #7ED1C2; }
.status-low .status-title { color: #2F3E46; }

/* Warning: #F2C94C */
.status-mid {
    background: #FFFCF2;
    border-color: #F2C94C;
}
.status-mid .status-icon { color: #F2C94C; }
.status-mid .status-title { color: #5C4E0C; }

/* Critical: #E57373 */
.status-high {
    background: #FFF5F5;
    border-color: #E57373;
    animation: pulse 2s infinite;
}
.status-high .status-icon { color: #E57373; }
.status-high .status-title { color: #781E1E; }

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(229, 115, 115, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(229, 115, 115, 0); }
    100% { box-shadow: 0 0 0 0 rgba(229, 115, 115, 0); }
}

/* --- Vital Box --- */
.vital-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
}

.vital-box {
    background: #F4FAFB; /* Light Aqua */
    border: 1px solid #DCE8EA;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    transition: transform 0.2s;
}

.vital-box:hover {
    transform: scale(1.02);
    border-color: #4FA6B3;
}

.vital-icon {
    font-size: 32px;
    margin-bottom: 8px;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
}

.vital-value {
    font-size: 26px;
    font-weight: 700;
    color: #4FA6B3;
}

/* --- Clean Up UI --- */
.main { max-width: 480px !important; margin: 0 auto; }
.block-container { padding-top: 0 !important; padding-bottom: 3rem !important; }
header, footer { visibility: hidden; }
</style>
"""

# 2. القيم الافتراضية
LOW_PRESET = {
    "baseline_temp_c": 36.7, "last_temp": 36.7,
    "baseline_hr_bpm": 70, "last_hr": 72,
    "baseline_spo2": 98.0, "last_spo2": 98.0,
    "baseline_crp_mg_l": 0.5,
}

MID_PRESET = {
    "baseline_temp_c": 37.2, "last_temp": 37.6,
    "baseline_hr_bpm": 75, "last_hr": 88,
    "baseline_spo2": 97.0, "last_spo2": 96.0,
    "baseline_crp_mg_l": 2.5,
}

HIGH_PRESET = {
    "baseline_temp_c": 37.8, "last_temp": 38.5,
    "baseline_hr_bpm": 95, "last_hr": 118,
    "baseline_spo2": 94.0, "last_spo2": 91.0,
    "baseline_crp_mg_l": 12.0,
}

# 3. مستويات الخطر (تم تحديث الألوان لتوافق التصميم الجديد)
RISK_LEVELS = {
    0: {
        'name_ar': 'حالة مستقرة',
        'name_en': 'Stable',
        'icon': '🛡️',
        'color': 'low', # Maps to #7ED1C2
        'message_ar': 'المؤشرات الحيوية ممتازة',
        'message_en': 'Vital signs are excellent'
    },
    1: {
        'name_ar': 'انتباه',
        'name_en': 'Warning',
        'icon': '⚠️',
        'color': 'mid', # Maps to #F2C94C
        'message_ar': 'يرجى التواصل مع الطبيب',
        'message_en': 'Please consult your doctor'
    },
    2: {
        'name_ar': 'تدخل عاجل',
        'name_en': 'Critical',
        'icon': '🚑',
        'color': 'high', # Maps to #E57373
        'message_ar': 'توجه للطوارئ فوراً',
        'message_en': 'Proceed to ER immediately'
    }
}import streamlit as st

# 1. تصميم الواجهة (CSS) بناءً على الـ Design System الجديد
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

/* --- Global Settings --- */
* {
    font-family: 'Cairo', sans-serif;
    color: #2F3E46; /* Primary Text: Dark Desaturated Blue-Gray */
}

/* --- Background Gradient (Top -> Bottom) --- */
/* Top: #FFFFFF, Middle: #F1F8F9, Bottom: #E3F0F2 */
.stApp {
    background: linear-gradient(180deg, #FFFFFF 0%, #F1F8F9 50%, #E3F0F2 100%);
    background-attachment: fixed;
}

/* --- Typography --- */
h1, h2, h3 {
    color: #4FA6B3 !important; /* Primary Teal */
    font-weight: 700;
}

p, label, .stMarkdown {
    color: #6B7C85; /* Secondary Text: Muted Gray-Blue */
}

/* --- Containers & Cards (Glass-morphism) --- */
/* White with 80-95% opacity, soft shadow, rounded corners */
.card, .stForm, div[data-testid="stVerticalBlock"] > div {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid #DCE8EA; /* Almost invisible border */
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0px 8px 24px rgba(79, 166, 179, 0.12); /* Soft Medical Shadow */
    backdrop-filter: blur(10px);
}

/* --- Logo Container --- */
.logo-container {
    text-align: center;
    padding: 40px 20px;
    /* Gradient: Left #6FBFC7 -> Right #4FA6B3 */
    background: linear-gradient(135deg, #6FBFC7 0%, #4FA6B3 100%);
    margin: -1rem -1rem 30px -1rem;
    border-radius: 0 0 40px 40px;
    box-shadow: 0px 10px 30px rgba(79, 166, 179, 0.2);
}

.app-title {
    color: white !important;
    font-size: 36px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.app-subtitle {
    color: rgba(255,255,255,0.95) !important;
    font-size: 16px;
    font-weight: 300;
}

/* --- Buttons (Primary Action) --- */
.stButton > button {
    width: 100%;
    /* Gradient: Left #6FBFC7 -> Right #4FA6B3 */
    background: linear-gradient(135deg, #6FBFC7 0%, #4FA6B3 100%);
    color: white !important;
    border: none;
    border-radius: 16px;
    padding: 16px;
    font-size: 18px;
    font-weight: 600;
    box-shadow: 0 8px 20px rgba(79, 166, 179, 0.25);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(79, 166, 179, 0.35);
}

/* --- Inputs --- */
.stTextInput > div > div > input {
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid #DCE8EA;
    border-radius: 12px;
    color: #2F3E46;
    height: 50px;
}

.stTextInput > div > div > input:focus {
    border-color: #4FA6B3;
    box-shadow: 0 0 0 2px rgba(79, 166, 179, 0.2);
}

/* --- Status Cards --- */
.status-card {
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    margin: 20px 0;
    border: 1px solid;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

/* Success: #7ED1C2 */
.status-low {
    background: #F4FAFB; 
    border-color: #7ED1C2;
}
.status-low .status-icon { color: #7ED1C2; }
.status-low .status-title { color: #2F3E46; }

/* Warning: #F2C94C */
.status-mid {
    background: #FFFCF2;
    border-color: #F2C94C;
}
.status-mid .status-icon { color: #F2C94C; }
.status-mid .status-title { color: #5C4E0C; }

/* Critical: #E57373 */
.status-high {
    background: #FFF5F5;
    border-color: #E57373;
    animation: pulse 2s infinite;
}
.status-high .status-icon { color: #E57373; }
.status-high .status-title { color: #781E1E; }

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(229, 115, 115, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(229, 115, 115, 0); }
    100% { box-shadow: 0 0 0 0 rgba(229, 115, 115, 0); }
}

/* --- Vital Box --- */
.vital-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin: 16px 0;
}

.vital-box {
    background: #F4FAFB; /* Light Aqua */
    border: 1px solid #DCE8EA;
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    transition: transform 0.2s;
}

.vital-box:hover {
    transform: scale(1.02);
    border-color: #4FA6B3;
}

.vital-icon {
    font-size: 32px;
    margin-bottom: 8px;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
}

.vital-value {
    font-size: 26px;
    font-weight: 700;
    color: #4FA6B3;
}

/* --- Clean Up UI --- */
.main { max-width: 480px !important; margin: 0 auto; }
.block-container { padding-top: 0 !important; padding-bottom: 3rem !important; }
header, footer { visibility: hidden; }
</style>
"""

# 2. القيم الافتراضية
LOW_PRESET = {
    "baseline_temp_c": 36.7, "last_temp": 36.7,
    "baseline_hr_bpm": 70, "last_hr": 72,
    "baseline_spo2": 98.0, "last_spo2": 98.0,
    "baseline_crp_mg_l": 0.5,
}

MID_PRESET = {
    "baseline_temp_c": 37.2, "last_temp": 37.6,
    "baseline_hr_bpm": 75, "last_hr": 88,
    "baseline_spo2": 97.0, "last_spo2": 96.0,
    "baseline_crp_mg_l": 2.5,
}

HIGH_PRESET = {
    "baseline_temp_c": 37.8, "last_temp": 38.5,
    "baseline_hr_bpm": 95, "last_hr": 118,
    "baseline_spo2": 94.0, "last_spo2": 91.0,
    "baseline_crp_mg_l": 12.0,
}

# 3. مستويات الخطر (تم تحديث الألوان لتوافق التصميم الجديد)
RISK_LEVELS = {
    0: {
        'name_ar': 'حالة مستقرة',
        'name_en': 'Stable',
        'icon': '🛡️',
        'color': 'low', # Maps to #7ED1C2
        'message_ar': 'المؤشرات الحيوية ممتازة',
        'message_en': 'Vital signs are excellent'
    },
    1: {
        'name_ar': 'انتباه',
        'name_en': 'Warning',
        'icon': '⚠️',
        'color': 'mid', # Maps to #F2C94C
        'message_ar': 'يرجى التواصل مع الطبيب',
        'message_en': 'Please consult your doctor'
    },
    2: {
        'name_ar': 'تدخل عاجل',
        'name_en': 'Critical',
        'icon': '🚑',
        'color': 'high', # Maps to #E57373
        'message_ar': 'توجه للطوارئ فوراً',
        'message_en': 'Proceed to ER immediately'
    }
}
