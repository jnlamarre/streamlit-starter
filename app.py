import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Component imports
from utils.icon_loader import load_icon_simple, load_icon_advanced
from utils.css_loader import load_css
from components.header import render_header
from components.footer import render_footer


st.set_page_config(
    page_title="Analytics Hub Enterprise | HQ Geosciences",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'mailto:support@hqgeosciences.com',
        'Report a bug': 'mailto:analytics-team@hqgeosciences.com',
        'About': "**Analytics Hub Enterprise** | HQ Geosciences v2.1.0"
    }
)

def generate_sample_data():
    """Generate sample data for analytics dashboard"""
    
    # Time series data (6 months)
    dates = pd.date_range(
        start=datetime.now() - timedelta(days=180),
        end=datetime.now(),
        freq='D'
    )
    
    # Mock data for revenue
    np.random.seed(42)
    ca_data = np.random.randn(len(dates)).cumsum() + 100
    
    # Mock data for regions
    regions = ['North', 'South', 'East', 'West']
    sales = [80, 95, 88, 105]
    
    df_ca = pd.DataFrame({
        'Date': dates,
        'CA': ca_data
    })
    
    df_regions = pd.DataFrame({
        'Region': regions,
        'Sales': sales
    })
    
    return df_ca, df_regions

def main():
    # ===== STYLING =====
    load_css([
        "static/styles/themes.css",
        "static/styles/components/shared.css",
        "static/styles/components/header.css", 
        "static/styles/components/footer.css",
        "static/styles/main.css"
    ])
    
    # ===== HEADER =====
    render_header("Production Analytics",
                  logo_path="app/static/images/logo/logo.png")
    
    # ===== DATA PREPARATION =====
    df_ca, df_regions = generate_sample_data()
    
    # ===== MAIN CONTENT =====
    # Main KPIs
    st.html('<div class="card section">')
    st.subheader("Production Indicators")

    st.html("""
    <div class="metrics-grid">
        <div class="metric-card positive">
            <div class="metric-icon">💰</div>
            <div class="metric-label">Revenue (YTD)</div>
            <div class="metric-value">12,8M€</div>
            <div class="metric-change positive">
                <span>↗</span> +18%
            </div>
        </div>
        
        <div class="metric-card positive">
            <div class="metric-icon">📊</div>
            <div class="metric-label">Market Share</div>
            <div class="metric-value">23,4%</div>
            <div class="metric-change positive">
                <span>↗</span> +2,1%
            </div>
        </div>
        
        <div class="metric-card negative highlight">
            <div class="metric-icon">😊</div>
            <div class="metric-label">Customer Satisfaction</div>
            <div class="metric-value">92,1%</div>
            <div class="metric-change negative">
                <span>↘</span> -1,3%
            </div>
        </div>
        
        <div class="metric-card positive">
            <div class="metric-icon">⚡</div>
            <div class="metric-label">Operational Efficiency</div>
            <div class="metric-value">87%</div>
            <div class="metric-change positive">
                <span>↗</span> +5%
            </div>
        </div>
    </div>
    """)

    st.html('</div>')

    # Time Series Analysis
    st.html('<div class="card section">')
    st.markdown(f'## {load_icon_advanced("chart-line", 24, "#1e40af")} Time Series Analysis', unsafe_allow_html=True)
    st.write("Revenue Evolution")
    st.html('<span class="badge badge-info">30-day trend</span>')

    fig_line = px.line(df_ca, x='Date', y='CA', 
                       color_discrete_sequence=['#1e40af'])
    fig_line.update_layout(
        showlegend=False,
        xaxis_title="Date",
        yaxis_title="Revenue"
    )
    st.plotly_chart(fig_line, use_container_width=True)
    st.html('</div>')

    # Regional Performance
    st.html('<div class="card section">')
    st.markdown(f'## {load_icon_advanced("chart-bar", 24, "#1e40af")} Regional Performance', unsafe_allow_html=True)
    st.write("Sales by Region")
    st.html('<span class="badge badge-success">Targets achieved</span>')

    fig_bar = px.bar(df_regions, x='Region', y='Sales',
                     color_discrete_sequence=['#1e40af'])
    fig_bar.update_layout(
        showlegend=False,
        xaxis_title="",
        yaxis_title="Sales (K$)"
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    st.html('</div>')

    # ===== FOOTER =====
    render_footer()

if __name__ == "__main__":
    main()