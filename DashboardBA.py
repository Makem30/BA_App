import streamlit as st
import pandas as pd
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Calculer le total des ventes
total_ventes = data['Montant'].sum()

# Afficher le KPI dans Streamlit
st.metric(label="Total des ventes", value=f"{total_ventes:.2f} €")
