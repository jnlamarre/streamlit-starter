import streamlit as st
from datetime import datetime


def render_footer(
    company_name: str = "HQ Geosciences Analytics Platform",
    version: str = "2.1.0"
):
    """Footer for executive dashboards - Styled via footer.css"""
    
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    st.html(f'''
    <div class="footer">
        <div class="footer-content">
            <p>🏢 {company_name}</p>
            <p>Data as of: {current_date} | Enterprise v{version}</p>
        </div>
    </div>
    ''')