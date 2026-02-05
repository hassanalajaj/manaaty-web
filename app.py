import streamlit as st
# نستورد الألوان والتصميم من ملف الإعدادات
try:
    from config import CUSTOM_CSS, COLORS
except ImportError:
    CUSTOM_CSS = ""
    COLORS = {"primary": "#1A5F7A"} # لون احتياطي

st.set_page_config(page_title="Manaaty | مناعتي", page_icon="🧬", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- إضافة اللوقو في الأعلى ---
# استخدمنا الأعمدة لوضع اللوقو في المنتصف بشكل أنيق
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # تأكد أن اسم الملف مطابق للموجود في مجلد assets
    # يمكنك التحكم في الحجم بتغيير width
    st.image("assets/logo.png", width=150) 

st.markdown(f"<h1 style='text-align: center; color: {COLORS['primary']}; margin-top: -20px;'>مناعتي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #607D8B;'>نظام الكشف المبكر عن العدوى</p>", unsafe_allow_html=True)
st.markdown("---")

# --- باقي محتوى الصفحة الأولى (مثلاً تسجيل الدخول) ---
# (أكمل بقية الكود الخاص بك هنا، مثل حقول الإدخال والأزرار)
# مثال بسيط:
st.markdown('<div class="mobile-box" style="background: white; text-align: center;">', unsafe_allow_html=True)
st.text_input("رقم الملف الطبي", placeholder="ID")
st.text_input("كلمة المرور", type="password", placeholder="Password")
st.button("تسجيل الدخول", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
