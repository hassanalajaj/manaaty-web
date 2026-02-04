
# app_patient_medical.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from config import CUSTOM_CSS, LOW_PRESET, MODERATE_PRESET, HIGH_PRESET, CLINICAL_ACTIONS
from ml_engine import load_and_train_model, compute_slope
import os

# ==================== CONFIG ====================
st.set_page_config(
    page_title="Manaaty | مناعتي",
    layout="centered",
    page_icon="🧬",
    initial_sidebar_state="collapsed"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ==================== SESSION INIT ====================
def init_session():
    if "patient_name" not in st.session_state:
        st.session_state.patient_name = "أحمد محمد العلي"
        st.session_state.patient_id = "P-24589"
        st.session_state.language = "ar"
        st.session_state.last_check = datetime.now() - timedelta(hours=2, minutes=15)
        st.session_state.device_battery = 84
        st.session_state.device_days_remaining = 4
        st.session_state.next_replace_date = "2026-02-08"
        
        # Load preset
        for k, v in MODERATE_PRESET.items():
            st.session_state[k] = v

init_session()
lang = st.session_state.language

# ==================== LOAD MODEL ====================
@st.cache_resource
def load_model_cached():
    return load_and_train_model()

model, base_model, metrics, feature_cols = load_model_cached()

# ==================== LANGUAGE TOGGLE ====================
col_lang1, col_lang2, col_lang3 = st.columns([1, 6, 1])
with col_lang3:
    if st.button("🌐", key="lang_btn", help="Switch Language"):
        st.session_state.language = "en" if lang == "ar" else "ar"
        st.rerun()

# ==================== HEADER ====================
st.markdown(f"""
<div class="app-header">
    {'<div style="font-size:60px; margin-bottom:10px;">🧬</div>' if not os.path.exists("logo.png") else '<img src="logo.png" class="app-logo">'}
    <h1 class="app-title">{"مناعتي" if lang == "ar" else "Manaaty"}</h1>
    <p class="app-subtitle">{"نظام الكشف المبكر عن العدوى" if lang == "ar" else "Early Infection Detection System"}</p>
</div>
""", unsafe_allow_html=True)

# ==================== PATIENT CARD ====================
st.markdown(f"""
<div class="patient-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <p class="patient-name">{"مرحباً، " if lang == "ar" else "Hello, "}{st.session_state.patient_name}</p>
            <p class="patient-id">{"رقم المريض" if lang == "ar" else "Patient ID"}: {st.session_state.patient_id}</p>
        </div>
        <div style="font-size: 40px;">👨‍⚕️</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== DEVICE STATUS ====================
hours_ago = int((datetime.now() - st.session_state.last_check).total_seconds() / 3600)
next_check_hours = 4 - hours_ago
minutes_component = int((datetime.now() - st.session_state.last_check).total_seconds() % 3600 / 60)

st.markdown(f"""
<div class="device-status-bar">
    <div class="device-item">
        <span class="device-item-icon">⏱️</span>
        <div class="device-item-label">{"آخر قياس" if lang == "ar" else "Last Check"}</div>
        <div class="device-item-value">{hours_ago}{"س " if lang == "ar" else "h "}{minutes_component}{"د" if lang == "ar" else "m"}</div>
    </div>
    <div class="device-item">
        <span class="device-item-icon">🔄</span>
        <div class="device-item-label">{"القياس القادم" if lang == "ar" else "Next Check"}</div>
        <div class="device-item-value">{next_check_hours}{"س" if lang == "ar" else "h"}</div>
    </div>
    <div class="device-item">
        <span class="device-item-icon">🔋</span>
        <div class="device-item-label">{"البطارية" if lang == "ar" else "Battery"}</div>
        <div class="device-item-value">{st.session_state.device_battery}%</div>
    </div>
    <div class="device-item">
        <span class="device-item-icon">📅</span>
        <div class="device-item-label">{"استبدال بعد" if lang == "ar" else "Replace in"}</div>
        <div class="device-item-value">{st.session_state.device_days_remaining}{"د" if lang == "ar" else "d"}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== QUICK TEST (DEMO) ====================
st.markdown(f"""
<div class="medical-card">
    <h3 class="card-title">
        <span class="card-title-icon">🧪</span>
        {"اختبار سريع (للتجربة)" if lang == "ar" else "Quick Test (Demo)"}
    </h3>
    <div class="quick-test-grid">
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✅\n" + ("طبيعي" if lang == "ar" else "Normal"), key="test_low", use_container_width=True):
        for k, v in LOW_PRESET.items():
            st.session_state[k] = v
        st.rerun()

with col2:
    if st.button("⚠️\n" + ("متوسط" if lang == "ar" else "Moderate"), key="test_mod", use_container_width=True):
        for k, v in MODERATE_PRESET.items():
            st.session_state[k] = v
        st.rerun()

with col3:
    if st.button("🚨\n" + ("خطر" if lang == "ar" else "High"), key="test_high", use_container_width=True):
        for k, v in HIGH_PRESET.items():
            st.session_state[k] = v
        st.rerun()

st.markdown("</div></div>", unsafe_allow_html=True)

# ==================== VITAL SIGNS ====================
def get_vital_status(value, normal_range):
    if value < normal_range[0] * 0.85 or value > normal_range[1] * 1.15:
        return 'critical'
    elif value < normal_range[0] * 0.95 or value > normal_range[1] * 1.05:
        return 'elevated'
    return 'normal'

vitals = [
    {
        'icon': '🌡️',
        'label_ar': 'درجة الحرارة',
        'label_en': 'Temperature',
        'value': st.session_state.last_temp,
        'unit': '°C',
        'range': (36.0, 37.5)
    },
    {
        'icon': '💓',
        'label_ar': 'نبضات القلب',
        'label_en': 'Heart Rate',
        'value': st.session_state.last_hr,
        'unit': 'bpm',
        'range': (60, 100)
    },
    {
        'icon': '🫁',
        'label_ar': 'مستوى الأكسجين',
        'label_en': 'Oxygen Level',
        'value': st.session_state.last_spo2,
        'unit': '%',
        'range': (95, 100)
    },
    {
        'icon': '🔬',
        'label_ar': 'بروتين CRP',
        'label_en': 'CRP Protein',
        'value': st.session_state.baseline_crp_mg_l,
        'unit': 'mg/L',
        'range': (0, 3)
    }
]

st.markdown(f"""
<div class="medical-card">
    <h3 class="card-title">
        <span class="card-title-icon">📊</span>
        {"مؤشراتك الحيوية الحالية" if lang == "ar" else "Your Current Vital Signs"}
    </h3>
    <div class="vital-grid">
""", unsafe_allow_html=True)

for vital in vitals:
    status = get_vital_status(vital['value'], vital['range'])
    label = vital['label_ar'] if lang == 'ar' else vital['label_en']
    
    st.markdown(f"""
    <div class="vital-box {status}">
        <span class="vital-icon">{vital['icon']}</span>
        <div class="vital-label">{label}</div>
        <div class="vital-value">{vital['value']:.1f}<span class="vital-unit">{vital['unit']}</span></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ==================== ANALYZE BUTTON ====================
if st.button(
    "🔍 " + ("تحليل حالتي الآن" if lang == "ar" else "Analyze My Status Now"),
    type="primary",
    use_container_width=True
):
    with st.spinner("🤖 " + ("جاري التحليل بالذكاء الاصطناعي..." if lang == "ar" else "AI is analyzing your data...")):
        # Compute slopes
        temp_slope = compute_slope(st.session_state.baseline_temp_c, st.session_state.last_temp)
        hr_slope = compute_slope(st.session_state.baseline_hr_bpm, st.session_state.last_hr)
        spo2_slope = compute_slope(st.session_state.baseline_spo2, st.session_state.last_spo2)
        rr_slope = compute_slope(st.session_state.baseline_rr_bpm, st.session_state.last_rr)
        hrv_slope = compute_slope(st.session_state.baseline_hrv_rmssd_ms, st.session_state.last_hrv)
        act_slope = compute_slope(st.session_state.baseline_activity_index, st.session_state.last_activity)
        
        input_data = {
            "age": st.session_state.age,
            "baseline_temp_c": st.session_state.baseline_temp_c,
            "baseline_hr_bpm": st.session_state.baseline_hr_bpm,
            "baseline_hrv_rmssd_ms": st.session_state.baseline_hrv_rmssd_ms,
            "baseline_spo2": st.session_state.baseline_spo2,
            "baseline_rr_bpm": st.session_state.baseline_rr_bpm,
            "baseline_activity_index": st.session_state.baseline_activity_index,
            "baseline_crp_mg_l": st.session_state.baseline_crp_mg_l,
            "baseline_il6_pg_ml": st.session_state.baseline_il6_pg_ml,
            "baseline_tnf_alpha_pg_ml": st.session_state.baseline_tnf_alpha_pg_ml,
            "baseline_ferritin_ng_ml": st.session_state.baseline_ferritin_ng_ml,
            "baseline_lymph_pct": st.session_state.baseline_lymph_pct,
            "baseline_neutro_pct": st.session_state.baseline_neutro_pct,
            "temp_slope_0_24": temp_slope,
            "hr_slope_0_24": hr_slope,
            "spo2_slope_0_24": spo2_slope,
            "hrv_slope_0_24": hrv_slope,
            "rr_slope_0_24": rr_slope,
            "activity_slope_0_24": act_slope,
        }
        
        input_df = pd.DataFrame([input_data])
        
        try:
            pred_class = int(model.predict(input_df)[0])
            pred_proba = model.predict_proba(input_df)[0]
            
            action = CLINICAL_ACTIONS[pred_class]
            
            # ==================== STATUS BADGE ====================
            title = action['title_ar'] if lang == 'ar' else action['title_en']
            message = action['message_ar'] if lang == 'ar' else action['message_en']
            
            st.markdown(f"""
            <div class="status-indicator status-{action['status']}">
                <span class="status-icon">{action['icon']}</span>
                <div>
                    <div style="font-size: 18px;">{title}</div>
                    <div style="font-size: 13px; margin-top: 4px; font-weight: 400;">{message}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Confidence
            st.markdown(f"""
            <div style="text-align: center; margin: 16px 0;">
                <span style="color: var(--text-secondary); font-size: 14px;">
                    {"دقة التحليل" if lang == "ar" else "Analysis Confidence"}:
                </span>
                <span style="color: var(--primary-teal); font-size: 22px; font-weight: 700; margin-left: 8px;">
                    {pred_proba[pred_class]*100:.0f}%
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            # ==================== INSTRUCTIONS ====================
            instructions = action['instructions_ar'] if lang == 'ar' else action['instructions_en']
            list_class = action['status']
            
            st.markdown(f"""
            <div class="instruction-list {list_class}">
                <h4>{"📋 ماذا يجب أن تفعل الآن؟" if lang == "ar" else "📋 What Should You Do Now?"}</h4>
                <ul>
                    {''.join([f'<li>{inst}</li>' for inst in instructions])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # ==================== ACTION BUTTONS ====================
            if action['buttons']:
                st.markdown('<div class="medical-card">', unsafe_allow_html=True)
                
                for btn in action['buttons']:
                    btn_label = btn['label_ar'] if lang == 'ar' else btn['label_en']
                    btn_style_class = f"btn-{btn['style']}"
                    
                    if st.button(btn_label, key=f"action_{btn['type']}", use_container_width=True):
                        if btn['type'] == 'emergency':
                            st.success("☎️ " + ("جاري الاتصال بالإسعاف 997..." if lang == "ar" else "Calling ambulance 997..."))
                            st.balloons()
                        elif btn['type'] == 'call':
                            st.success("📞 " + ("جاري الاتصال بالعيادة..." if lang == "ar" else "Calling clinic..."))
                        elif btn['type'] == 'book':
                            st.success("✅ " + ("تم إرسال طلب الموعد العاجل" if lang == "ar" else "Urgent appointment request sent"))
                        elif btn['type'] == 'map':
                            st.success("🗺️ " + ("فتح خريطة أقرب مستشفى..." if lang == "ar" else "Opening nearest hospital map..."))
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            # ==================== NOTIFICATIONS (HIGH RISK) ====================
            if pred_class == 2:
                st.markdown(f"""
                <div class="medical-card">
                    <h3 class="card-title">
                        <span class="card-title-icon">✅</span>
                        {"تم الإبلاغ تلقائياً" if lang == "ar" else "Automatically Notified"}
                    </h3>
                    
                    <div class="notification-card">
                        <span class="notification-icon">👨‍⚕️</span>
                        <div class="notification-text">
                            <strong>{"د. أحمد السعيد" if lang == "ar" else "Dr. Ahmed Al-Saeed"}</strong><br>
                            {"طبيب الأورام المعالج" if lang == "ar" else "Treating Oncologist"}
                        </div>
                    </div>
                    
                    <div class="notification-card">
                        <span class="notification-icon">🏥</span>
                        <div class="notification-text">
                            <strong>{"قسم الطوارئ" if lang == "ar" else "Emergency Department"}</strong><br>
                            {"مستشفى الملك فيصل التخصصي" if lang == "ar" else "King Faisal Specialist Hospital"}
                        </div>
                    </div>
                    
                    <div class="notification-card">
                        <span class="notification-icon">📱</span>
                        <div class="notification-text">
                            <strong>{"محمد أحمد (أخ)" if lang == "ar" else "Mohammed Ahmed (Brother)"}</strong><br>
                            {"جهة الاتصال الطارئة" if lang == "ar" else "Emergency Contact"}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ {'خطأ في التحليل' if lang == 'ar' else 'Analysis Error'}: {str(e)}")

# ==================== FOOTER ====================
st.markdown(f"""
<div class="app-footer">
    <p style="font-weight: 600; margin-bottom: 8px;">
        {"مناعتي - نظام الكشف المبكر عن العدوى" if lang == "ar" else "Manaaty - Early Infection Detection System"}
    </p>
    <p style="margin-bottom: 8px;">
        {"تم التطوير في جامعة الملك سعود للعلوم الصحية" if lang == "ar" else "Developed at King Saud University for Health Sciences"}
    </p>
    <p style="font-size: 11px; color: var(--text-secondary);">
        {"⚠️ هذا النظام مساعد طبي ولا يغني عن استشارة الطبيب المختص" if lang == "ar" else "⚠️ This system is a medical assistant and doesn't replace specialist consultation"}
    </p>
    <p style="margin-top: 12px; font-size: 11px;">
        {"آخر تحديث" if lang == "ar" else "Last Updated"}: {datetime.now().strftime("%Y-%m-%d %H:%M")}
    </p>
</div>
""", unsafe_allow_html=True)
