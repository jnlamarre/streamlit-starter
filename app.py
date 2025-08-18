import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Sidebar
st.sidebar.header("🧭 Navigation")

st.sidebar.write("Période")
st.sidebar.selectbox("", ["30j"], label_visibility="collapsed")

st.sidebar.write("🔧 Mode debug")

# Titre principal
st.title("Analytics Dashboard")
st.write("Dashboard de performance commerciale")

# KPIs Principaux
st.subheader("KPIs Principaux")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Chiffre d'Affaires", "$2,88M", "12%")

with col2:
    st.metric("Commandes Total", "8,834", "5%")

with col3:
    st.metric("Clients Moyens/Jour", "199", "-2%")

with col4:
    st.metric("Panier Moyen", "€327", "8%")

# Analyses Temporelles
st.subheader("Analyses Temporelles")
st.write("Evolution du Chiffre d'Affaires")

# Données factices pour le graphique
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
ca_data = np.random.randn(len(dates)).cumsum() + 100

df_ca = pd.DataFrame({
    'Date': dates,
    'CA': ca_data
})

# Graphique en ligne
fig_line = px.line(df_ca, x='Date', y='CA', 
                   color_discrete_sequence=['#87CEEB'])
fig_line.update_layout(
    showlegend=False,
    xaxis_title="Date",
    yaxis_title="CA"
)
st.plotly_chart(fig_line, use_container_width=True)

# Performance par Région
st.subheader("Performance par Région")
st.write("Ventes par Région")

# Données factices pour les barres
regions = ['Nord', 'Sud', 'Est', 'Ouest']
ventes = [80, 95, 88, 105]

df_regions = pd.DataFrame({
    'Région': regions,
    'Ventes': ventes
})

# Graphique en barres
fig_bar = px.bar(df_regions, x='Région', y='Ventes',
                 color_discrete_sequence=['#87CEEB'])
fig_bar.update_layout(
    showlegend=False,
    xaxis_title="",
    yaxis_title="Ventes (K€)"
)
st.plotly_chart(fig_bar, use_container_width=True)