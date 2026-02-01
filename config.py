# config.py

# 1. CSS Design (Mobile App Style - Modern & Clean)
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

html, body { font-family: 'Inter', sans-serif; font-size: 16px; background-color: #0f111a; }
.stApp { background-color: #0f111a; }

/* إخفاء عناصر ستريم ليت الافتراضية لجعل التطبيق يبدو حقيقياً */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Card Style imitating Mobile Cards */
.mobile-card {
    background: #1e2130;
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    border: 1px solid #2d324a;
}

/* Typography */
h1, h2, h3 { color: #ffffff; letter-spacing: -0.5px; }
p { color: #a0a6c0; line-height: 1.6; }

/* Status Indicators */
.status-badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 99px;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 12px;
}
.status-low { background: #1b4d3e; color: #4ade80; border: 1px solid #22c55e; }
.status-mod { background: #452c15; color: #fbbf24; border: 1px solid #f59e0b; }
.status-high { background: #4c1d1d; color: #f87171; border: 1px solid #ef4444; animation: pulse 2s infinite; }

/* Action Plan Steps */
.step-box {
    background: rgba(255,255,255,0.05);
    border-left: 4px solid #5c6cff;
    padding: 16px;
    margin: 12px 0;
    border-radius: 0 12px 12px 0;
}
.step-number { font-weight: bold; color: #5c6cff; font-size: 18px; margin-right: 8px; }

/* Animations */
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
    100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

/* Button Styling */
.stButton>button {
    width: 100%;
    border-radius: 16px;
    height: 55px;
    font-size: 18px;
    font-weight: 600;
    background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
    border: none;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
    transition: transform 0.2s;
}
.stButton>button:hover {
    transform: scale(1.02);
}
</style>
"""

# 2. Presets (Patient Data Simulators)
LOW_PRESET = {
    "age": 25, "sex": "Male",
    "baseline_crp_mg_l": 0.5, "baseline_il6_pg_ml": 0.3, "baseline_tnf_alpha_pg_ml": 1.5,
    "baseline_ferritin_ng_ml": 75.0, "baseline_lymph_pct": 35.0, "baseline_neutro_pct": 50.0,
    "baseline_temp_c": 36.7, "last_temp": 36.7,
    "baseline_hr_bpm": 70, "last_hr": 70,
    "baseline_rr_bpm": 14, "last_rr": 14,
    "baseline_spo2": 98.0, "last_spo2": 98.0,
    "baseline_hrv_rmssd_ms": 60.0, "last_hrv": 60.0,
    "baseline_activity_index": 0.6, "last_activity": 0.6,
}

MODERATE_PRESET = {
    "age": 35, "sex": "Male",
    "baseline_crp_mg_l": 1.2, "baseline_il6_pg_ml": 0.8, "baseline_tnf_alpha_pg_ml": 2.0,
    "baseline_ferritin_ng_ml": 100.0, "baseline_lymph_pct": 30.0, "baseline_neutro_pct": 58.0,
    "baseline_temp_c": 36.8, "last_temp": 37.0,
    "baseline_hr_bpm": 72, "last_hr": 76,
    "baseline_rr_bpm": 14, "last_rr": 16,
    "baseline_spo2": 98.0, "last_spo2": 97.0,
    "baseline_hrv_rmssd_ms": 60.0, "last_hrv": 50.0,
    "baseline_activity_index": 0.6, "last_activity": 0.5,
}

HIGH_PRESET = {
    "age": 55, "sex": "Male",
    "baseline_crp_mg_l": 8.0, "baseline_il6_pg_ml": 6.0, "baseline_tnf_alpha_pg_ml": 10.0,
    "baseline_ferritin_ng_ml": 300.0, "baseline_lymph_pct": 20.0, "baseline_neutro_pct": 70.0,
    "baseline_temp_c": 37.5, "last_temp": 38.2,
    "baseline_hr_bpm": 90, "last_hr": 110,
    "baseline_rr_bpm": 20, "last_rr": 28,
    "baseline_spo2": 95.0, "last_spo2": 92.0,
    "baseline_hrv_rmssd_ms": 50.0, "last_hrv": 25.0,
    "baseline_activity_index": 0.5, "last_activity": 0.2,
}

# 3. Patient Guidance (PROACTIVE STEPS - Patient Centric)
# هنا التغيير الكبير: نخاطب المريض ونقول له ماذا يفعل بالضبط
PATIENT_GUIDANCE = {
    0: {
        "title": "You are doing great! 🌟",
        "color": "green",
        "steps": [
            "Your immune system looks stable.",
            "Keep wearing the patch for continuous monitoring.",
            "No extra action needed today."
        ]
    },
    1: {
        "title": "Attention Needed ⚠️",
        "color": "orange",
        "steps": [
            "We detected slight changes in your vitals.",
            "Please rest and drink plenty of water.",
            "Monitor your temperature every 6 hours.",
            "If you feel worse, contact your care provider."
        ]
    },
    2: {
        "title": "URGENT ACTION REQUIRED 🚨",
        "color": "red",
        "steps": [
            "High inflammation markers detected.",
            "**Go to the Emergency Room / Clinic immediately.**",
            "Show this screen to the triage nurse.",
            "Do not wait or sleep on it."
        ]
    }
}
