import streamlit as st
# استدعاء ملف التصميم
try:
    from config import CUSTOM_CSS
except:
    CUSTOM_CSS = ""

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

# تطبيق التنسيق
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# تنسيقات خاصة بهذه الصفحة فقط (لجعلها تشبه الجوال)
st.markdown("""
<style>
/* إزاحة المحتوى للأعلى */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 5rem !important;
}

/* شريط البحث */
.search-box {
    background: white;
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    color: #90A4AE;
    display: flex;
    align-items: center;
    border: 1px solid #ECEFF1;
}

/* البطاقات المربعة (الشبكة) */
.grid-card {
    border-radius: 25px;
    padding: 20px;
    height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.03);
    transition: transform 0.2s;
    margin-bottom: 15px;
    cursor: pointer;
}
.grid-card:hover { transform: scale(1.02); }

/* ألوان البطاقات */
.card-teal { background: #004D40; color: white; }
.card-light { background: #E0F7FA; color: #006064; }
.card-purple { background: #E8EAF6; color: #3949AB; }
.card-green { background: #E0F2F1; color: #00695C; }

/* البطاقة العريضة السفلية */
.card-wide {
    background: linear-gradient(90deg, #42A5F5 0%, #1E88E5 100%);
    border-radius: 20px;
    padding: 20px;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 8px 20px rgba(33, 150, 243, 0.25);
    margin-top: 10px;
}

/* القائمة السفلية العائمة */
.bottom-nav {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: white;
    padding: 10px 30px;
    border-radius: 40px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    display: flex;
    gap: 40px;
    z-index: 1000;
}
.nav-icon { font-size: 24px; cursor: pointer; opacity: 0.5; }
.nav-icon.active { opacity: 1; color: #004D40; transform: scale(1.2); }
</style>
""", unsafe_allow_html=True)

# --- المحتوى ---

# 1. الترحيب
st.markdown(f"<h3 style='text-align: right; margin-bottom: 10px;'>مرحباً، {st.session_state.get('patient_id', 'عبير')} 👋</h3>", unsafe_allow_html=True)

# 2. شريط البحث الوهمي
st.markdown("""
<div class="search-box">
    <span style="margin-left:10px;">🔍</span> بحث في التقارير...
</div>
""", unsafe_allow_html=True)

# 3. الشبكة (المربعات)
col1, col2 = st.columns(2)

with col1:
    # تقارير التحاليل (غامق)
    st.markdown("""
    <div class="grid-card card-teal">
        <div style="font-size:35px; margin-bottom:10px;">📄</div>
        <div style="font-weight:bold;">التقارير الطبية</div>
        <div style="font-size:12px; opacity:0.8;">آخر تحديث: اليوم</div>
    </div>
    """, unsafe_allow_html=True)
    
    # نمط الحياة (بنفسجي فاتح)
    st.markdown("""
    <div class="grid-card card-purple">
        <div style="font-size:35px; margin-bottom:10px;">🍎</div>
        <div style="font-weight:bold;">نمط الحياة</div>
        <div style="font-size:12px; opacity:0.8;">نصائح يومية</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # رفع تقارير (أزرق فاتح)
    st.markdown("""
    <div class="grid-card card-light">
        <div style="font-size:35px; margin-bottom:10px;">📤</div>
        <div style="font-weight:bold;">رفع تقرير</div>
        <div style="font-size:12px; opacity:0.8;">pdf, jpg</div>
    </div>
    """, unsafe_allow_html=True)
    
    # التوصيات (أخضر فاتح)
    st.markdown("""
    <div class="grid-card card-green">
        <div style="font-size:35px; margin-bottom:10px;">🛡️</div>
        <div style="font-weight:bold;">التوصيات</div>
        <div style="font-size:12px; opacity:0.8;">3 تنبيهات جديدة</div>
    </div>
    """, unsafe_allow_html=True)

# 4. مصادر تثقيفية (عريض)
st.markdown("""
<div class="card-wide">
    <div>
        <div style="font-weight:bold; font-size:18px;">مصادر تثقيفية</div>
        <div style="font-size:12px; opacity:0.9;">تعرف أكثر على حالتك</div>
    </div>
    <div style="font-size:30px;">📚</div>
</div>
""", unsafe_allow_html=True)

# 5. القائمة السفلية
st.markdown("""
<div class="bottom-nav">
    <div class="nav-icon">👤</div>
    <div class="nav-icon active">🏠</div>
    <div class="nav-icon">⚙️</div>
</div>
""", unsafe_allow_html=True)
