# config.py

# 1. CSS Design (Dark Mode & Animations)
CUSTOM_CSS = """
<style>
html, body { font-size: 16px; }
body { background-color: #050713; color: #e4e6eb; }
.main { background-color: #050713; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1400px; }
.m-card { background: radial-gradient(circle at top left, #1b2140 0, #0c0f1c 45%, #050713 100%); border-radius: 18px; padding: 20px 22px; border: 1px solid #242a43; box-shadow: 0 0 24px rgba(0, 200, 255, 0.12); margin-bottom: 18px; }
.m-title { font-size: 22px; font-weight: 600; color: #d0dcff; margin-bottom: 12px; }
section[data-testid="stSidebar"] { background: #060815; border-right: 1px solid #15182b; font-size: 15px; }
.stNumberInput label, .stTextInput label, .stSelectbox label { color: #b8bedc !important; font-weight: 500 !important; }
.stButton>button { border-radius: 999px; padding: 12px 24px; background: linear-gradient(135deg, #303553, #191b2b); color: #fff; border: 1px solid #414872; transition: all 0.3s ease; }
.stButton>button:hover { background: linear-gradient(135deg, #3b4270, #20233a); border-color: #5c6cff; transform: translateY(-2px); }
.risk-card { border-radius: 16px; padding: 20px; margin-top: 10px; font-size: 15px; }
.risk-low { background: rgba(46, 204, 113, 0.12); border: 2px solid rgba(46, 204, 113, 0.5); color: #2ecc71; }
.risk-mod { background: rgba(243, 156, 18, 0.12); border: 2px solid rgba(243, 156, 18, 0.5); color: #f1c40f; }
.risk-high { background: rgba(231, 76, 60, 0.18); border: 3px solid rgba(231, 76, 60, 0.8); color: #ff6b6b; animation: pulse-border 2s infinite; }
@keyframes pulse-border { 0%, 100% { border-color: rgba(231, 76, 60, 0.8); box-shadow: 0 0 20px rgba(231, 76, 60, 0.3); } 50% { border-color: rgba(231, 76, 60, 1); box-shadow: 0 0 30px rgba(231, 76, 60, 0.6); } }
.urgent-alert { background: linear-gradient(135deg, #ff4444, #cc0000); border: 3px solid #ff0000; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 20px; animation: pulse-alert 2s infinite; }
@keyframes pulse-alert { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.85; transform: scale(1.02); } }
.vital-pill { display: flex; justify-content: space-between; align-items: center; background: rgba(15, 20, 45, 0.95); border-radius: 12px; padding: 10px 14px; margin-bottom: 6px; border: 1px solid #222849; font-size: 15px; color: #dde3ff; }
.vital-label { display: flex; align-items: center; gap: 8px; }
.metric-card { background: rgba(30, 35, 70, 0.6); border-radius: 10px; padding: 12px; text-align: center; border: 1px solid #2a3555; }
.metric-label { font-size: 12px; color: #8892b8; margin-bottom: 4px; }
.metric-value { font-size: 20px; font-weight: 700; color: #5c6cff; }
</style>
"""

# 2. Presets (Matched to YOUR CSV Columns)
LOW_PRESET = {
    "age": 25, "sex": "Male",
    # Biomarkers
    "baseline_crp_mg_l": 0.5, "baseline_il6_pg_ml": 0.3, "baseline_tnf_alpha_pg_ml": 1.5,
    "baseline_ferritin_ng_ml": 75.0, "baseline_lymph_pct": 35.0, "baseline_neutro_pct": 50.0,
    # Vitals (Baseline from CSV + Last for UI)
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

# 3. Clinical Recommendations
CLINICAL_RECOMMENDATIONS = {
    0: ["✅ Continue routine monitoring", "✅ Next assessment in 24 hours", "✅ Maintain current treatment plan", "✅ Patient can remain in outpatient care"],
    1: ["⚠️ Increase monitoring frequency to every 12 hours", "⚠️ Consider CBC with differential", "⚠️ Review recent medication changes", "⚠️ Assess for potential infection sources", "⚠️ Monitor temperature trends closely"],
    2: ["🚨 **IMMEDIATE** clinical review required", "🚨 Consider blood cultures and sensitivity", "🚨 Evaluate for empiric broad-spectrum antibiotics", "🚨 Check vital signs every 4 hours", "🚨 Prepare for possible hospital admission", "🚨 Consult infectious disease specialist"]
}
