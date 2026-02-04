import streamlit as st

# CSS - تنسيقات التصميم العام
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

/* الخط العام والاتجاه */
* {
    font-family: 'Cairo', sans-serif;
}

/* خلفية التطبيق - تدرج لوني هادئ جداً */
.stApp {
    background: linear-gradient(180deg, #F0F4F8 0%, #E2EBF0 100%);
    background-attachment: fixed;
}

/* إخفاء القوائم الافتراضية العلوية والسفلية */
#MainMenu, footer, header {visibility: hidden;}

/* تحسين شكل النصوص */
h1, h2, h3 {
    color: #0E5159 !important;
    font-weight: 700;
}

p {
    color: #546E7A;
}
</style>
"""
