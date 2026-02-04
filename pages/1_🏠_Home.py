import streamlit as st
from config import CUSTOM_CSS

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

# تطبيق CSS العام + تخصيصات إضافية لهذه الصفحة فقط
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
/* إخفاء الهيدر الافتراضي لتقريب التصميم من الجوال */
header {visibility: hidden;}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 5rem !important; /* مساحة للبار السفلي */
}

/* تنسيق شريط البحث */
.search-container {
    background: white;
    border-radius: 15px;
    padding: 10px 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    color: #888;
}

/* تنسيق الشبكة (الزر المربع) */
.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-bottom: 15px;
}

.grid-card {
    border-radius: 24px;
    padding: 20px;
    height: 160px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    transition: transform 0.2s;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    text-decoration: none; /* إزالة الخط من الروابط */
}

.grid-card:hover {
    transform: scale(1.03);
}

/* الألوان حسب الصورة المرفقة */
.card-dark-teal {
    background-color: #0E5159; /* تيل غامق */
    color: white !important;
}

.card-lavender {
    background-color: #DCEAF2; /* سماوي فاتح جداً */
    color: #0E5159 !important;
}

.card-purple {
    background-color: #9FA8DA; /* بنفسجي هادئ */
    color: white !important;
}

.card-green {
    background-color: #80CBC4; /* أخضر تيفاني */
    color: white !important;
}

.card-wide {
    background: linear-gradient(90deg, #64B5F6 0%, #42A5F5 100%);
    border-radius: 20px;
    padding: 20px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 10px;
    box-shadow: 0 4px 15px rgba(33, 150, 243, 0.2);
}

/* الأيقونات والنصوص */
.card-icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.card-title {
    font-size: 16px;
    font-weight: 700;
    line-height: 1.4;
}

.card-subtitle {
    font-size: 12px;
    opacity: 0.9;
    font-weight: normal;
}

/* البار السفلي العائم (Bottom Navigation) */
.bottom-nav {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: white;
    width: 250px;
    height: 60px;
    border-radius: 30px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    display: flex;
    justify-content: space-around;
    align-items: center;
    z-index: 999;
}

.nav-item {
    font-size: 24px;
    color: #B0BEC5;
    cursor: pointer;
}

.nav-item.active {
    background-color: #0E5159;
    color: white;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 10px rgba(14, 81, 89, 0.3);
}

</style>
""", unsafe_allow_html=True)

# --- المحتوى ---

# 1. الترحيب (Header)
st.markdown(f"<h2 style='text-align: right; color: #0E5159; margin-bottom: 20px;'>مرحباً، {st.session_state.get('patient_id', 'عبير')} 👋</h2>", unsafe_allow_html=True)

# 2. شريط البحث (Fake Search Bar)
st.markdown("""
<div class="search-container">
    <span style="font-size: 20px; margin-left: 10px;">🔍</span>
    <span>ابحث في التقارير الطبية...</span>
</div>
""", unsafe_allow_html=True)

# 3. الشبكة (The Grid) - هنا وزعنا البيانات التي طلبتها على شكل أزرار
col1, col2 = st.columns(2)

with col1:
    # الكارت 1: (غامق) - يمثل "تقارير التحاليل" أو الـ Risk & Vitals
    st.markdown("""
    <div class="grid-card card-dark-teal">
        <div class="card-icon">📄</div>
        <div class="card-title">بياناتي الحيوية</div>
        <div class="card-subtitle">الخطر: ⚠️ مرتفع</div>
    </div>
    """, unsafe_allow_html=True)
    
    # الكارت 3: (بنفسجي) - يمثل "نمط الحياة" أو الـ Trend
    st.markdown("""
    <div class="grid-card card-purple">
        <div class="card-icon">📈</div>
        <div class="card-title">سجل القراءات</div>
        <div class="card-subtitle">تحليل النمط</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # الكارت 2: (فاتح) - يمثل "رفع تقارير" أو الـ Demographics
    st.markdown("""
    <div class="grid-card card-lavender">
        <div class="card-icon">👤</div>
        <div class="card-title">الملف الشخصي</div>
        <div class="card-subtitle">Demographics</div>
    </div>
    """, unsafe_allow_html=True)
    
    # الكارت 4: (أخضر تيفاني) - يمثل "التوصيات"
    st.markdown("""
    <div class="grid-card card-green">
        <div class="card-icon">🛡️</div>
        <div class="card-title">التوصيات</div>
        <div class="card-subtitle">3 تنبيهات جديدة</div>
    </div>
    """, unsafe_allow_html=True)

# 4. الكارت العريض (Wide Card) - مصادر تثقيفية / أو اتصل بالطبيب
st.markdown("""
<div class="card-wide">
    <div>
        <div style="font-weight: bold; font-size: 18px;">📞 اتصل بالطبيب</div>
        <div style="font-size: 13px; opacity: 0.9;">فريقنا متاح 24/7 للمساعدة</div>
    </div>
    <div style="font-size: 35px;">🩺</div>
</div>
""", unsafe_allow_html=True)

# 5. البار السفلي (Bottom Navigation)
st.markdown("""
<div class="bottom-nav">
    <div class="nav-item">👤</div>
    <div class="nav-item active">🏠</div>
    <div class="nav-item">⚙️</div>
</div>
""", unsafe_allow_html=True)
