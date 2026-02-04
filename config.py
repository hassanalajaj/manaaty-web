# config.py

# ==================== MEDICAL-GRADE CSS ====================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

* {
    font-family: 'Cairo', 'Segoe UI', sans-serif;
    -webkit-font-smoothing: antialiased;
}

:root {
    --primary-teal: #1a7f8e;
    --primary-light: #e8f4f8;
    --accent-blue: #4a90a4;
    --success-green: #7ec8a3;
    --warning-orange: #f4a261;
    --danger-red: #e76f51;
    --bg-gradient-start: #f0f9fb;
    --bg-gradient-end: #e1f0f5;
    --card-shadow: rgba(26, 127, 142, 0.08);
    --text-primary: #2c3e50;
    --text-secondary: #546e7a;
    --border-color: #d4e4e8;
}

html, body {
    background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
    color: var(--text-primary);
    font-size: 16px;
    margin: 0;
    padding: 0;
}

.main {
    background: transparent;
    max-width: 480px !important;
    margin: 0 auto;
    padding: 0 !important;
}

.block-container {
    padding: 0.5rem 1rem !important;
}

/* Hide Sidebar */
section[data-testid="stSidebar"] {
    display: none;
}

/* ==================== HEADER ==================== */
.app-header {
    background: linear-gradient(135deg, var(--primary-teal) 0%, #156270 100%);
    padding: 24px 20px 100px 20px;
    margin: -1rem -1rem 0 -1rem;
    text-align: center;
    position: relative;
    border-radius: 0 0 30px 30px;
    box-shadow: 0 4px 20px rgba(26, 127, 142, 0.2);
}

.app-logo {
    width: 70px;
    height: 70px;
    margin: 0 auto 12px auto;
    display: block;
    filter: brightness(0) invert(1);
}

.app-title {
    font-size: 28px;
    font-weight: 700;
    color: white;
    margin: 0;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.app-subtitle {
    font-size: 14px;
    color: rgba(255,255,255,0.9);
    margin-top: 6px;
    font-weight: 300;
}

.patient-card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    margin: -70px 10px 20px 10px;
    box-shadow: 0 8px 30px var(--card-shadow);
    position: relative;
    z-index: 10;
}

.patient-name {
    font-size: 20px;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
}

.patient-id {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 4px;
}

/* ==================== STATUS BADGE ==================== */
.status-indicator {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 16px;
    border-radius: 16px;
    margin: 16px 0;
    font-weight: 600;
    font-size: 16px;
}

.status-normal {
    background: linear-gradient(135deg, #d4f1e8 0%, #e8f8f2 100%);
    border: 2px solid #7ec8a3;
    color: #2d6a4f;
}

.status-warning {
    background: linear-gradient(135deg, #ffecd1 0%, #fff5e6 100%);
    border: 2px solid #f4a261;
    color: #bc6c25;
}

.status-danger {
    background: linear-gradient(135deg, #ffd4cf 0%, #ffe5e2 100%);
    border: 2px solid #e76f51;
    color: #a94438;
    animation: pulse-danger 2s infinite;
}

@keyframes pulse-danger {
    0%, 100% { 
        transform: scale(1);
        box-shadow: 0 4px 20px rgba(231, 111, 81, 0.2);
    }
    50% { 
        transform: scale(1.02);
        box-shadow: 0 6px 30px rgba(231, 111, 81, 0.4);
    }
}

.status-icon {
    font-size: 28px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

/* ==================== CARD STYLES ==================== */
.medical-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    margin: 16px 0;
    box-shadow: 0 4px 15px var(--card-shadow);
    border: 1px solid var(--border-color);
}

.card-title {
    font-size: 18px;
    font-weight: 600;
    color: var(--primary-teal);
    margin: 0 0 16px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-title-icon {
    font-size: 22px;
}

/* ==================== VITAL SIGNS ==================== */
.vital-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 12px 0;
}

.vital-box {
    background: linear-gradient(135deg, var(--primary-light) 0%, #f7fcfd 100%);
    border-radius: 14px;
    padding: 16px;
    text-align: center;
    border: 1px solid rgba(26, 127, 142, 0.15);
    transition: all 0.3s ease;
}

.vital-box:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(26, 127, 142, 0.12);
}

.vital-box.elevated {
    background: linear-gradient(135deg, #fff5e6 0%, #fef9f0 100%);
    border-color: var(--warning-orange);
}

.vital-box.critical {
    background: linear-gradient(135deg, #ffe5e2 0%, #fff0ee 100%);
    border-color: var(--danger-red);
}

.vital-icon {
    font-size: 32px;
    margin-bottom: 8px;
    display: block;
}

.vital-label {
    font-size: 12px;
    color: var(--text-secondary);
    margin-bottom: 6px;
    font-weight: 400;
}

.vital-value {
    font-size: 24px;
    font-weight: 700;
    color: var(--primary-teal);
    line-height: 1;
}

.vital-unit {
    font-size: 13px;
    color: var(--text-secondary);
    font-weight: 400;
    margin-left: 2px;
}

/* ==================== DEVICE STATUS ==================== */
.device-status-bar {
    background: linear-gradient(135deg, #f0f9fb 0%, #e8f4f8 100%);
    border-radius: 14px;
    padding: 14px 18px;
    margin: 16px 0;
    border: 1px solid var(--border-color);
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.device-item {
    text-align: center;
    flex: 1;
}

.device-item-icon {
    font-size: 20px;
    display: block;
    margin-bottom: 4px;
    opacity: 0.7;
}

.device-item-label {
    font-size: 10px;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.device-item-value {
    font-size: 16px;
    font-weight: 700;
    color: var(--primary-teal);
    margin-top: 2px;
}

/* ==================== BUTTONS ==================== */
.btn-primary {
    background: linear-gradient(135deg, var(--primary-teal) 0%, #156270 100%);
    color: white;
    padding: 16px 24px;
    border-radius: 14px;
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(26, 127, 142, 0.25);
    transition: all 0.3s ease;
    width: 100%;
    margin: 8px 0;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 127, 142, 0.35);
}

.btn-success {
    background: linear-gradient(135deg, #7ec8a3 0%, #6bb892 100%);
}

.btn-warning {
    background: linear-gradient(135deg, #f4a261 0%, #e38f4f 100%);
}

.btn-danger {
    background: linear-gradient(135deg, #e76f51 0%, #d45940 100%);
    animation: pulse-btn-danger 1.5s infinite;
}

@keyframes pulse-btn-danger {
    0%, 100% { box-shadow: 0 4px 15px rgba(231, 111, 81, 0.25); }
    50% { box-shadow: 0 6px 25px rgba(231, 111, 81, 0.45); }
}

.btn-outline {
    background: white;
    color: var(--primary-teal);
    border: 2px solid var(--primary-teal);
}

/* ==================== INSTRUCTION LIST ==================== */
.instruction-list {
    background: linear-gradient(135deg, #f7fcfd 0%, #eef7f9 100%);
    border-radius: 14px;
    padding: 20px;
    margin: 16px 0;
    border-left: 4px solid var(--primary-teal);
}

.instruction-list h4 {
    color: var(--primary-teal);
    font-size: 16px;
    margin: 0 0 14px 0;
    font-weight: 600;
}

.instruction-list ul {
    margin: 0;
    padding-left: 20px;
}

.instruction-list li {
    margin: 10px 0;
    line-height: 1.6;
    color: var(--text-primary);
    font-size: 14px;
}

.instruction-list.warning {
    background: linear-gradient(135deg, #fff9f0 0%, #fff5e6 100%);
    border-left-color: var(--warning-orange);
}

.instruction-list.warning h4 {
    color: var(--warning-orange);
}

.instruction-list.danger {
    background: linear-gradient(135deg, #fff0ee 0%, #ffe5e2 100%);
    border-left-color: var(--danger-red);
}

.instruction-list.danger h4 {
    color: var(--danger-red);
}

/* ==================== NOTIFICATION CARD ==================== */
.notification-card {
    background: linear-gradient(135deg, #e8f4f8 0%, #d4ebf2 100%);
    border-radius: 14px;
    padding: 16px;
    margin: 12px 0;
    border: 1px solid var(--primary-teal);
    display: flex;
    align-items: center;
    gap: 12px;
}

.notification-icon {
    font-size: 24px;
    color: var(--primary-teal);
}

.notification-text {
    flex: 1;
    font-size: 14px;
    color: var(--text-primary);
}

/* ==================== LANGUAGE TOGGLE ==================== */
.lang-toggle {
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid var(--border-color);
    border-radius: 25px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 600;
    color: var(--primary-teal);
    cursor: pointer;
    z-index: 1000;
    box-shadow: 0 2px 10px var(--card-shadow);
}

/* ==================== QUICK TEST BUTTONS ==================== */
.quick-test-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 16px 0;
}

.quick-test-btn {
    background: white;
    border: 2px solid var(--border-color);
    border-radius: 12px;
    padding: 14px 8px;
    text-align: center;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.quick-test-btn:hover {
    transform: translateY(-2px);
    border-color: var(--primary-teal);
    box-shadow: 0 4px 12px var(--card-shadow);
}

.quick-test-btn.normal {
    border-color: #7ec8a3;
    color: #2d6a4f;
}

.quick-test-btn.warning {
    border-color: #f4a261;
    color: #bc6c25;
}

.quick-test-btn.danger {
    border-color: #e76f51;
    color: #a94438;
}

/* ==================== FOOTER ==================== */
.app-footer {
    text-align: center;
    padding: 24px 16px;
    color: var(--text-secondary);
    font-size: 12px;
    border-top: 1px solid var(--border-color);
    margin-top: 30px;
    background: rgba(255, 255, 255, 0.5);
}

/* ==================== STREAMLIT OVERRIDES ==================== */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, var(--primary-teal) 0%, #156270 100%);
    color: white !important;
    border: none;
    border-radius: 14px;
    padding: 16px;
    font-size: 16px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(26, 127, 142, 0.25);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(26, 127, 142, 0.35);
}

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.viewerBadge_container__1QSob {display: none;}

</style>
"""

# ==================== PRESETS ====================
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
    "baseline_crp_mg_l": 2.5, "baseline_il6_pg_ml": 1.2, "baseline_tnf_alpha_pg_ml": 3.0,
    "baseline_ferritin_ng_ml": 150.0, "baseline_lymph_pct": 28.0, "baseline_neutro_pct": 62.0,
    "baseline_temp_c": 37.2, "last_temp": 37.6,
    "baseline_hr_bpm": 75, "last_hr": 88,
    "baseline_rr_bpm": 16, "last_rr": 18,
    "baseline_spo2": 97.0, "last_spo2": 96.0,
    "baseline_hrv_rmssd_ms": 55.0, "last_hrv": 45.0,
    "baseline_activity_index": 0.5, "last_activity": 0.4,
}

HIGH_PRESET = {
    "age": 55, "sex": "Male",
    "baseline_crp_mg_l": 12.0, "baseline_il6_pg_ml": 8.0, "baseline_tnf_alpha_pg_ml": 15.0,
    "baseline_ferritin_ng_ml": 400.0, "baseline_lymph_pct": 18.0, "baseline_neutro_pct": 75.0,
    "baseline_temp_c": 37.8, "last_temp": 38.5,
    "baseline_hr_bpm": 95, "last_hr": 118,
    "baseline_rr_bpm": 22, "last_rr": 28,
    "baseline_spo2": 94.0, "last_spo2": 91.0,
    "baseline_hrv_rmssd_ms": 40.0, "last_hrv": 22.0,
    "baseline_activity_index": 0.4, "last_activity": 0.15,
}

# ==================== CLINICAL ACTIONS ====================
CLINICAL_ACTIONS = {
    0: {
        'status': 'normal',
        'icon': '✅',
        'title_ar': 'حالتك مطمئنة',
        'title_en': 'You\'re Doing Great',
        'message_ar': 'جميع مؤشراتك ضمن المعدل الطبيعي',
        'message_en': 'All your vital signs are within normal range',
        'instructions_ar': [
            '✓ استمر في نشاطك اليومي المعتاد',
            '✓ تناول الأدوية في مواعيدها المحددة',
            '✓ اشرب كمية كافية من الماء',
            '✓ القياس التالي التلقائي بعد 4 ساعات',
            '✓ يمكنك طلب قياس إضافي في أي وقت'
        ],
        'instructions_en': [
            '✓ Continue your normal daily activities',
            '✓ Take medications as scheduled',
            '✓ Stay well hydrated',
            '✓ Next automatic check in 4 hours',
            '✓ You can request additional check anytime'
        ],
        'buttons': []
    },
    
    1: {
        'status': 'warning',
        'icon': '⚠️',
        'title_ar': 'تحتاج متابعة طبية',
        'title_en': 'Medical Follow-up Needed',
        'message_ar': 'اكتشفنا بعض التغيرات في مؤشراتك الحيوية',
        'message_en': 'We detected some changes in your vital signs',
        'instructions_ar': [
            '📞 اتصل بفريقك الطبي اليوم (لا تؤجل)',
            '📅 احجز موعد عاجل في نفس اليوم',
            '🌡️ قس درجة حرارتك كل ساعتين',
            '💊 لا تغير جرعات الأدوية دون استشارة',
            '📝 سجل أي أعراض جديدة',
            '🚨 إذا ساءت الأعراض، توجه للطوارئ مباشرة'
        ],
        'instructions_en': [
            '📞 Call your medical team today (don\'t postpone)',
            '📅 Book urgent same-day appointment',
            '🌡️ Check temperature every 2 hours',
            '💊 Don\'t change medication doses without consultation',
            '📝 Log any new symptoms',
            '🚨 If symptoms worsen, go to ER immediately'
        ],
        'buttons': [
            {'label_ar': '📞 اتصل بالعيادة', 'label_en': '📞 Call Clinic', 'type': 'call', 'style': 'warning'},
            {'label_ar': '📅 احجز موعد', 'label_en': '📅 Book Appointment', 'type': 'book', 'style': 'outline'}
        ]
    },
    
    2: {
        'status': 'danger',
        'icon': '🚨',
        'title_ar': 'حالة طارئة - تصرف فوراً',
        'title_en': 'EMERGENCY - Act Immediately',
        'message_ar': 'مؤشرات تدل على احتمال وجود عدوى خطيرة',
        'message_en': 'Indicators suggest possible serious infection',
        'instructions_ar': [
            '🚨 توجه إلى قسم الطوارئ الآن (لا تتأخر)',
            '📱 أو اتصل بالإسعاف فوراً: 997',
            '🏥 عند الوصول، أخبر الممرضة:',
            '   "تنبيه من نظام مناعتي - مستوى خطر عالي"',
            '',
            '✅ تم إبلاغ فريقك الطبي تلقائياً',
            '✅ تم إرسال بياناتك لقسم الطوارئ',
            '✅ تم إبلاغ جهات الاتصال الطارئة',
            '',
            '⚠️ لا تنتظر - العدوى قد تتفاقم بسرعة شديدة'
        ],
        'instructions_en': [
            '🚨 Go to Emergency Room NOW (don\'t delay)',
            '📱 Or call Ambulance immediately: 997',
            '🏥 Upon arrival, tell the nurse:',
            '   "Manaaty Alert - High Risk Level"',
            '',
            '✅ Your medical team has been notified',
            '✅ Your data sent to ER',
            '✅ Emergency contacts have been alerted',
            '',
            '⚠️ Don\'t wait - infection can worsen very rapidly'
        ],
        'buttons': [
            {'label_ar': '🚨 اتصل بالإسعاف 997', 'label_en': '🚨 Call Ambulance 997', 'type': 'emergency', 'style': 'danger'},
            {'label_ar': '📍 أقرب مستشفى', 'label_en': '📍 Nearest Hospital', 'type': 'map', 'style': 'outline'}
        ]
    }
}
