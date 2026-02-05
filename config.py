import streamlit as st

# ==============================================
# 🎨 منطقة تعديل الألوان (ضع ألوانك الجديدة هنا)
# ==============================================
COLORS = {
    # اللون الرئيسي للعناوين والأيقونات (التيل الغامق)
    "primary": "#1A5F7A",  # <--- غير هذا الكود للون الجديد

    # ألوان الكروت الخلفية (الباستيل الهادئة)
    "card_teal": "#D1E9F6",    # <--- لون كرت العلامات الحيوية
    "card_lavender": "#D7D3F7", # <--- لون كرت الاتجاه العام
    "card_mint": "#B2E2D2",     # <--- لون كرت المؤشرات
    
    # لون الخطر (للأحمر)
    "danger": "#E53935",

    # خلفية التطبيق المتدرجة (من الأعلى للأسفل)
    "bg_top": "#FFFFFF",   # <--- لون البداية (أبيض)
    "bg_bottom": "#F0F7F9", # <--- لون النهاية (سماوي فاتح جداً)

    # لون النصوص
    "text_dark": "#000000", # للنصوص على خلفية بيضاء
    "text_light": "#FFFFFF" # للنصوص على خلفية غامقة
}
# ==============================================


# CSS - تنسيقات التصميم
CUSTOM_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

* {{ font-family: 'Cairo', sans-serif; direction: rtl; }}

/* تطبيق خلفية التدرج الجديدة */
.stApp {{
    background: linear-gradient(180deg, {COLORS["bg_top"]} 0%, {COLORS["bg_bottom"]} 100%);
    background-attachment: fixed;
}}

#MainMenu, footer, header {{visibility: hidden;}}

h1, h2, h3 {{
    color: {COLORS["primary"]} !important;
    font-weight: 700;
}}

/* تنسيق الكروت */
.mobile-box {{
    border-radius: 25px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    margin-bottom: 12px;
    border: 1px solid rgba(0,0,0,0.05);
}}

/* كلاسات مساعدة للألوان */
.text-black {{ color: {COLORS["text_dark"]} !important; }}
.bg-danger {{ background-color: {COLORS["danger"]} !important; color: white !important; }}

/* شريط التنقل */
.nav-bar {{
    position: fixed;
    bottom: 15px; left: 50%; transform: translateX(-50%);
    background: white; padding: 10px 40px; border-radius: 40px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    display: flex; gap: 50px; z-index: 1000;
}}
</style>
"""

# القيم الافتراضية (لتجنب الأخطاء في الصفحات الأخرى)
LOW_PRESET = {"last_temp": 36.6, "last_hr": 72, "last_spo2": 98, "baseline_crp_mg_l": 2.0}
MID_PRESET = {"last_temp": 37.5, "last_hr": 92, "last_spo2": 95, "baseline_crp_mg_l": 8.0}
HIGH_PRESET = {"last_temp": 38.8, "last_hr": 115, "last_spo2": 91, "baseline_crp_mg_l": 15.0}

RISK_LEVELS = {
    0: {'name_ar': 'مستقر', 'color': COLORS["card_mint"], 'icon': '✅'},
    1: {'name_ar': 'تنبيه', 'color': COLORS["card_lavender"], 'icon': '⚠️'},
    2: {'name_ar': 'خطر عالي', 'color': COLORS["danger"], 'icon': '🚨'}
}
