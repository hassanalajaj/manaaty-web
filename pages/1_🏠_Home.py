import streamlit as st
import pandas as pd
import numpy as np
from config import CUSTOM_CSS

st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# التحقق من تسجيل الدخول
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

# --- CSS إضافي خاص بهذه الصفحة لتقسيم البطاقات ---
st.markdown("""
<style>
/* تخصيص الألوان للكروت حسب الصورة */
.card-blue { background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); border: 1px solid #90CAF9; }
.card-purple { background: linear-gradient(135deg, #F3E5F5 0%, #E1BEE7 100%); border: 1px solid #CE93D8; }
.card-teal { background: linear-gradient(135deg, #E0F2F1 0%, #B2DFDB 100%); border: 1px solid #80CBC4; }
.card-risk { background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%); border: 1px solid #EF9A9A; }

.dashboard-title {
    color: #1A7F8E;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
.metric-label { font-size: 14px; color: #546E7A; }
.metric-value { font-size: 22px; font-weight: bold; color: #263238; }
.metric-change { font-size: 14px; font-weight: bold; }
.change-up { color: #E53935; } /* أحمر للارتفاع الخطر */
.change-down { color: #43A047; } /* أخضر للانخفاض الجيد */
</style>
""", unsafe_allow_html=True)

# --- الهيدر والترحيب ---
col_header_1, col_header_2 = st.columns([3, 1])
with col_header_1:
    st.markdown(f"### مرحباً، {st.session_state.get('patient_id', 'المريض')} 👋")
    st.caption("آخر تحديث: قبل 10 دقائق")

with col_header_2:
    if st.button("📞 اتصل بالطبيب", type="primary"):
        st.toast("تم إرسال طلب اتصال للطبيب المناوب 👨‍⚕️", icon="✅")

st.divider()

# --- محاكاة Popup التوصيات ---
if "popup_shown" not in st.session_state:
    st.toast("💡 توصية جديدة: يرجى شرب كميات مياه إضافية اليوم نظراً لارتفاع بسيط في الحرارة.", icon="ℹ️")
    st.session_state.popup_shown = True

# --- الصف الأول: تقييم الخطر + الترند (Risk & Trend) ---
c1, c2 = st.columns([1, 2])

with c1:
    st.markdown("""
    <div class="card card-risk" style="padding: 20px; border-radius: 20px; text-align: center; height: 100%;">
        <h4 style="color: #C62828;">مستوى الخطر (Risk Stratification)</h4>
        <h1 style="font-size: 50px;">High</h1>
        <p>⚠️ يتطلب مراقبة مستمرة</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card" style="padding: 20px; border-radius: 20px;">', unsafe_allow_html=True)
    st.markdown("##### 📈 المؤشر العام (Trend Analysis)")
    # رسم بياني وهمي
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Heat", "HR", "Infection"])
    st.line_chart(chart_data, height=150)
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصف الثاني: البيانات الحيوية والمؤشرات (Vitals & Biomarkers) ---
col_vitals, col_bio = st.columns(2)

# Vitals Box (Baseline vs Change)
with col_vitals:
    st.markdown('<div class="card card-purple" style="padding: 20px; border-radius: 20px;">', unsafe_allow_html=True)
    st.markdown("#### 🫀 العلامات الحيوية (Vitals)")
    
    # محاكاة جدول صغير
    vitals_html = """
    <table style="width:100%; text-align: center;">
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="text-align: right;">المؤشر</td>
            <td>الأساس (Baseline)</td>
            <td>الحالي (Current)</td>
            <td>التغيير</td>
        </tr>
        <tr>
            <td style="text-align: right;"><b>الحرارة</b></td>
            <td>36.5°</td>
            <td>37.8°</td>
            <td class="change-up">🔺 +1.3</td>
        </tr>
        <tr>
            <td style="text-align: right;"><b>النبض</b></td>
            <td>70 bpm</td>
            <td>95 bpm</td>
            <td class="change-up">🔺 +25</td>
        </tr>
         <tr>
            <td style="text-align: right;"><b>الضغط</b></td>
            <td>120/80</td>
            <td>118/78</td>
            <td class="change-down">🔻 Stable</td>
        </tr>
    </table>
    """
    st.markdown(vitals_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Biomarker Box
with col_bio:
    st.markdown('<div class="card card-teal" style="padding: 20px; border-radius: 20px;">', unsafe_allow_html=True)
    st.markdown("#### 🧬 المؤشرات الحيوية (Biomarkers)")
    
    bio_html = """
    <table style="width:100%; text-align: center;">
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="text-align: right;">التحليل</td>
            <td>الأساس (Baseline)</td>
            <td>الحالي (Current)</td>
            <td>التغيير</td>
        </tr>
        <tr>
            <td style="text-align: right;"><b>CRP</b></td>
            <td>2.0</td>
            <td>12.5</td>
            <td class="change-up">🔺 High</td>
        </tr>
        <tr>
            <td style="text-align: right;"><b>WBC</b></td>
            <td>4.5</td>
            <td>3.2</td>
            <td class="change-up">🔻 Low</td>
        </tr>
         <tr>
            <td style="text-align: right;"><b>Neutrophils</b></td>
            <td>2.1</td>
            <td>1.0</td>
            <td class="change-up">🔻 Critical</td>
        </tr>
    </table>
    """
    st.markdown(bio_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- الصف الثالث: التوصيات (يسار) وبيانات المريض (يمين) ---
# ملاحظة: في Streamlit الاتجاه الافتراضي Left->Right.
# لجعل الديموغرافيك يمين والتوصيات يسار، سنستخدم الأعمدة ونعكس المحتوى
col_recommend, col_demo = st.columns([1, 1])

# Left: Recommendations (التوصيات)
with col_recommend:
    st.markdown("""
    <div class="card card-blue" style="padding: 20px; border-radius: 20px; min-height: 150px;">
        <h4>📋 التوصيات الطبية</h4>
        <ul style="text-align: right; color: #455A64;">
            <li>تناول خافض حرارة كل 6 ساعات.</li>
            <li>إعادة فحص الدم (CBC) صباح الغد.</li>
            <li>البقاء في العزل المنزلي لتجنب العدوى.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Right: Patient Demographics (بيانات المريض)
with col_demo:
    st.markdown("""
    <div class="card" style="padding: 20px; border-radius: 20px; min-height: 150px; background: white; border: 1px solid #eee;">
        <h4 style="color: #1A7F8E;">👤 بيانات المريض</h4>
        <div style="display: flex; justify-content: space-between;">
            <div>
                <p class="metric-label">العمر</p>
                <p class="metric-value">45 سنة</p>
            </div>
            <div>
                <p class="metric-label">فصيلة الدم</p>
                <p class="metric-value">O+</p>
            </div>
             <div>
                <p class="metric-label">الوزن</p>
                <p class="metric-value">78 كجم</p>
            </div>
        </div>
        <hr>
        <p style="font-size: 12px; color: #888;">ID: 2849302 | الحالة: زراعة نخاع (يوم +14)</p>
    </div>
    """, unsafe_allow_html=True)
