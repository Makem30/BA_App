import streamlit as st
import pandas as pd
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Calculer le total des ventes
total_ventes = data['Montant'].sum()

# Afficher le KPI dans Streamlit

#-----------------------------------------------------------------------------------------------
# Calculer les KPI
# nombre_total_transactions = len(data)
# montant_moyen_transaction = data['Montant'].mean()
# satisfaction_client_moyenne = data['Satisfaction_Client'].mean()

# # Afficher les KPI dans Streamlit
# col1, col2, col3, col4 = st.columns([1.5,2,1.5,1.5], gap="large")  # Créer 3 colonnes pour afficher les KPI côte à côte


# with col1:
#     st.metric(label="Nombre total de transactions", value=nombre_total_transactions)

# with col2:
#     st.metric(label="Montant moyen par transaction", value=f"{montant_moyen_transaction:.2f} €")

# with col3:
#     st.metric(label="Satisfaction client moyenne", value=f"{satisfaction_client_moyenne:.2f}")
    
# with col4:
#     st.metric(label="Total des ventes", value=f"{total_ventes:.2f} €")

#-------------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .metric-container {
        background-color: white;
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Afficher les KPI dans les carrés
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(label="Nombre total de transactions", value=nombre_total_transactions)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(label="Montant moyen par transaction", value=f"{montant_moyen_transaction:.2f} €")
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(label="Satisfaction client moyenne", value=f"{satisfaction_client_moyenne:.2f}")
        st.markdown('</div>', unsafe_allow_html=True)
