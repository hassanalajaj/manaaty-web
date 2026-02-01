# config.py

# ==================== MOBILE-FIRST CSS ====================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

* { font-family: 'Cairo', sans-serif; }

/* الخلفية العامة للتطبيق */
.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #1a1f3a 100%);
    color: #e4e6eb;
}

/* إخفاء القوائم الجانبية والعناصر الافتراضية */
section[data-testid="stSidebar"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ====== Mobile Card ====== */
.mobile-card {
    background: linear-gradient(145deg, #1e2442 0%, #161a2e 100%);
    border-radius: 20px;
    padding: 20px;
    margin: 12px 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.05);
}

/* ====== Status Badges ====== */
.status-badge {
    display: inline-block;
    padding: 8px 20px;
    border-radius: 25px;
    font-size: 14px;
    font-weight: 600;
    margin: 8px 0;
}
.status-normal { background: linear-gradient(135deg, #00d4aa, #00a884); color: white; box-shadow: 0 4px 15px rgba(0, 212, 170, 0.3); }
.status-warning { background: linear-gradient(135deg, #ffb74d, #ff9800); color: white; box-shadow: 0 4px 15px rgba(255, 152, 0, 0.3); }
.status-danger { 
    background: linear-gradient(135deg, #ff5252, #f44336); 
    color: white; 
    box-shadow: 0 4px 15px rgba(255, 82, 82, 0.4);
    animation: pulse-danger 2s infinite; 
}

@keyframes pulse-danger {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(244, 67, 54, 0.7); }
    70% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(244, 67, 54, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(244, 67, 54, 0); }
}

/* ====== Vitals Rows ====== */
.vital-row {
    display: flex; justify-content: space-between; align-items: center;
    padding: 14px 16px; background: rgba(20, 25, 45, 0.6);
    border-radius: 14px; margin: 8px 0; border-left: 4px solid #4CAF50;
}
.vital-row.elevated { border-left-color: #FF9800; background: rgba(255, 152, 0, 0.08); }
.vital-row.critical { border-left-color: #f44336; background: rgba(244, 67, 54, 0.12); }
.vital-value { font-size: 20px; font-weight: 700; color: #ffffff; }

/* ====== Action Buttons ====== */
.action-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white; padding: 16px; border-radius: 16px;
    text-align: center; font-weight: 600; margin: 8px 0; cursor: pointer;
}
.action-btn-emergency {
    background: linear-gradient(135deg, #ff5252 0%, #c62828 100%);
    color: white; padding: 16px; border-radius: 16px;
    text-align: center; font-weight: 600; margin: 8px 0; cursor: pointer;
    animation: pulse-danger 1.5s infinite;
}

/* ====== Streamlit Button Override ====== */
.stButton > button {
    width: 100%; border-radius: 16px; height: 50px; border: none;
    font-weight: 700; font-size: 16px;
}
</style>
"""

# 2. PRESETS
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

# 3. CLINICAL ACTIONS
CLINICAL_ACTIONS = {
    0: { 
        'status': 'normal', 'badge': 'status-normal', 'icon': '✅',
        'title': 'كل شيء طبيعي', 'title_en': 'All Clear',
        'message': 'مؤشراتك الحيوية ضمن المعدل الطبيعي', 'message_en': 'Vital signs are normal',
        'instructions': {'ar': ['✓ استمر في نشاطك اليومي', '✓ القياس التالي بعد 4 ساعات'], 'en': ['✓ Continue daily activity', '✓ Next check in 4 hours']},
        'action_buttons': []
    },
    1: { 
        'status': 'warning', 'badge': 'status-warning', 'icon': '⚠️',
        'title': 'انتبه - تحتاج متابعة', 'title_en': 'Caution Needed',
        'message': 'تغيرات طفيفة في المؤشرات الحيوية', 'message_en': 'Slight vital signs changes',
        'instructions': {'ar': ['📞 اتصل بطبيبك اليوم', '🌡️ قس حرارتك كل ساعتين'], 'en': ['📞 Call doctor today', '🌡️ Check temp every 2 hours']},
        'action_buttons': [{'label': '📞 اتصل بالعيادة', 'label_en': '📞 Call Clinic', 'type': 'call'}]
    },
    2: { 
        'status': 'danger', 'badge': 'status-danger', 'icon': '🚨',
        'title': 'طوارئ - تحرك فوراً', 'title_en': 'EMERGENCY ACT NOW',
        'message': 'مؤشرات عدوى نشطة وخطيرة', 'message_en': 'Critical infection signs',
        'instructions': {'ar': ['🚨 توجه للطوارئ فوراً', '🚑 لا تنتظر أبداً'], 'en': ['🚨 Go to ER immediately', '🚑 Do not wait']},
        'action_buttons': [{'label': '🚑 اتصل بالإسعاف 997', 'label_en': '🚑 Call 997', 'type': 'emergency'}, {'label': '🏥 أقرب مستشفى', 'label_en': '🏥 Nearest ER', 'type': 'map'}]
    }
}
