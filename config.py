# config.py

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

* {
    font-family: 'Cairo', sans-serif;
}

:root {
    --teal: #1a7f8e;
    --teal-light: #e8f4f8;
    --green: #7ec8a3;
    --orange: #f4a261;
    --red: #e76f51;
    --bg: #f0f9fb;
    --card-bg: white;
    --text: #2c3e50;
    --text-light: #546e7a;
}

html, body {
    background: linear-gradient(135deg, #f0f9fb 0%, #e1f0f5 100%);
    color: var(--text);
}

.main {
    max-width: 500px !important;
    margin: 0 auto;
    padding: 0 !important;
}

.block-container {
    padding: 1rem !important;
}

/* Hide Streamlit elements */
#MainMenu, footer, header {visibility: hidden;}
section[data-testid="stSidebar"] {display: none;}

/* Logo Background */
.logo-container {
    text-align: center;
    padding: 30px 20px;
    background: linear-gradient(135deg, var(--teal) 0%, #156270 100%);
    margin: -1rem -1rem 20px -1rem;
    border-radius: 0 0 30px 30px;
}

.logo-img {
    width: 120px;
    height: 120px;
    margin: 0 auto;
    background: white;
    border-radius: 25px;
    padding: 15px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.app-title {
    color: white;
    font-size: 32px;
    font-weight: 700;
    margin-top: 20px;
}

.app-subtitle {
    color: rgba(255,255,255,0.9);
    font-size: 14px;
    margin-top: 8px;
}

/* Card */
.card {
    background: white;
    border-radius: 20px;
    padding: 24px;
    margin: 16px 0;
    box-shadow: 0 4px 20px rgba(26, 127, 142, 0.08);
    border: 1px solid #e8f4f8;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--teal);
    margin-bottom: 16px;
}

/* Status Cards */
.status-card {
    border-radius: 18px;
    padding: 24px;
    text-align: center;
    margin: 20px 0;
    border: 3px solid;
}

.status-low {
    background: linear-gradient(135deg, #d4f1e8 0%, #e8f8f2 100%);
    border-color: var(--green);
}

.status-mid {
    background: linear-gradient(135deg, #ffecd1 0%, #fff5e6 100%);
    border-color: var(--orange);
}

.status-high {
    background: linear-gradient(135deg, #ffd4cf 0%, #ffe5e2 100%);
    border-color: var(--red);
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.02); }
}

.status-icon {
    font-size: 60px;
    margin-bottom: 12px;
}

.status-title {
    font-size: 24px;
    font-weight: 700;
    margin: 12px 0;
}

.status-message {
    font-size: 14px;
    opacity: 0.8;
}

/* Vital Grid */
.vital-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
}

.vital-box {
    background: var(--teal-light);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    border: 2px solid transparent;
    transition: all 0.3s;
}

.vital-box:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(26, 127, 142, 0.15);
}

.vital-box.warning {
    background: #fff5e6;
    border-color: var(--orange);
}

.vital-box.danger {
    background: #ffe5e2;
    border-color: var(--red);
}

.vital-icon {
    font-size: 36px;
    margin-bottom: 8px;
}

.vital-label {
    font-size: 12px;
    color: var(--text-light);
    margin-bottom: 6px;
}

.vital-value {
    font-size: 28px;
    font-weight: 700;
    color: var(--teal);
}

/* Buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, var(--teal) 0%, #156270 100%);
    color: white;
    border: none;
    border-radius: 16px;
    padding: 16px;
    font-size: 16px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(26, 127, 142, 0.25);
    transition: all 0.3s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 127, 142, 0.35);
}

/* Device Status */
.device-bar {
    display: flex;
    justify-content: space-around;
    background: white;
    border-radius: 16px;
    padding: 16px;
    margin: 16px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.device-item {
    text-align: center;
}

.device-icon {
    font-size: 24px;
    opacity: 0.7;
}

.device-label {
    font-size: 11px;
    color: var(--text-light);
    margin-top: 4px;
}

.device-value {
    font-size: 18px;
    font-weight: 700;
    color: var(--teal);
    margin-top: 4px;
}

/* Icon Grid */
.icon-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 20px 0;
}

.icon-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    cursor: pointer;
    transition: all 0.3s;
}

.icon-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(26, 127, 142, 0.15);
}

.icon-card-icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.icon-card-label {
    font-size: 13px;
    color: var(--text);
    font-weight: 600;
}

/* Input */
.stTextInput input {
    border-radius: 12px;
    border: 2px solid var(--teal-light);
    padding: 14px;
    font-size: 16px;
}

.stTextInput input:focus {
    border-color: var(--teal);
}

</style>
"""

# Presets (only 3 states: Low, Mid, High)
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

RISK_LEVELS = {
    0: {
        'name_ar': 'حالة طبيعية',
        'name_en': 'Normal',
        'icon': '✅',
        'color': 'low',
        'message_ar': 'جميع مؤشراتك ضمن المعدل الطبيعي',
        'message_en': 'All vitals are normal'
    },
    1: {
        'name_ar': 'تحتاج متابعة',
        'name_en': 'Need Follow-up',
        'icon': '⚠️',
        'color': 'mid',
        'message_ar': 'اتصل بفريقك الطبي اليوم',
        'message_en': 'Contact your medical team today'
    },
    2: {
        'name_ar': 'حالة طارئة',
        'name_en': 'Emergency',
        'icon': '🚨',
        'color': 'high',
        'message_ar': 'توجه للطوارئ فوراً',
        'message_en': 'Go to ER immediately'
    }
}


