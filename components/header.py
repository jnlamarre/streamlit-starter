import streamlit as st

def render_header(
    report_title: str,
    logo_path: str = "static/images/logo/logo.png"
):
    """Corporate header with 3-column layout - Styled via header.css"""
    
    st.html(f'''
    <div class="custom-header">
        <div class="header-left">
            <img src="{logo_path}" alt="Logo" class="header-logo">
        </div>
        <div class="header-center">
            <h1 class="header-title">{report_title}</h1>
            <p class="header-subtitle">HQ Geosciences Dashboard | Q4 2024</p>
        </div>
        <div class="header-spacer">
            <!-- Space for balance -->
        </div>
    </div>
    ''')