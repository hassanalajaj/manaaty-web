import streamlit as st

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');

* {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

/* الخلفية المتدرجة الناعمة كما في الصورة */
.stApp {
    background: linear-gradient(180deg, #FFFFFF 0%, #F0F7F9 100%);
    background-attachment: fixed;
}

#MainMenu, footer, header {visibility: hidden;}

/* تنسيق النصوص */
h1, h2, h3 {
    color: #1A5F7A !important; /* لون تيل طبي هادئ */
    font-weight: 700;
}

/* تحسين شكل الحاويات لتبدو كأنها تطبيق جوال */
.block-container {
    max-width: 450px !important;
    padding-top: 2rem !important;
    padding-bottom: 6rem !important;
}
</style>
"""
