import streamlit as st
import pandas as pd
import altair as alt
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

#-----------------------------------------------------------------------------------------------
# Calculer les KPI
nombre_total_transactions = len(data)
montant_moyen_transaction = data['Montant'].mean()
satisfaction_client_moyenne = data['Satisfaction_Client'].mean()
total_ventes = data['Montant'].sum()
#-----------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .metric-container {
        background-color: #ffff; /* Bleu */
        border: none; /* Supprimer la bordure */
        padding: 30px;
        border-radius: 5px;
        color: black; /* Texte blanc */
        text-align: center; /* Centrer le texte */
    }
    .metric-label {
        font-size: 18px;
        font-weight: bold;
    }
    .metric-value {
        font-size: 24px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Afficher les KPI dans les carrés
col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown(
        f'<div class="metric-container"><div class="metric-label">Nombre total de transactions</div><div class="metric-value">{nombre_total_transactions}</div></div>',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f'<div class="metric-container"><div class="metric-label">Montant moyen par transaction</div><div class="metric-value">{montant_moyen_transaction:.2f} €</div></div>',
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f'<div class="metric-container"><div class="metric-label">Satisfaction client moyenne</div><div class="metric-value">{satisfaction_client_moyenne:.2f}</div></div>',
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f'<div class="metric-container"><div class="metric-label">total_ventes</div><div class="metric-value">{total_ventes:.2f}</div></div>',
        unsafe_allow_html=True,
    ) 
#-------------------------------------------------------------------------------------------
# Convertir la colonne 'date' en datetime
# data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# data['date'] = pd.to_datetime(data['date'])

# # Grouper les données par date et calculer les ventes totales quotidiennes
# daily_sales = data.groupby('date')['sales'].sum().reset_index()

# # Créer le graphique en courbe
# st.line_chart(daily_sales, x='date', y='sales')
#-------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import altair as alt

# Charger les données
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Convertir la colonne 'Date_Transaction' en datetime
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])

# Grouper les données par date et magasin, puis calculer le total des ventes
daily_sales = data.groupby(['Date_Transaction', 'Magasin'])['Montant'].sum().reset_index()

# Créer le graphique avec Altair
chart = alt.Chart(daily_sales).mark_line().encode(
    x='Date_Transaction:T',
    y='Montant:Q',
    color='Magasin:N'
).properties(
    title='Ventes quotidiennes de tous les magasins',
    width=800,
    height=400
)

# Afficher le graphique sur Streamlit
st.altair_chart(chart, use_container_width=True)
#------------------------------------------------------------------------------
# Calculer le total des ventes par magasin
sales_by_store = data.groupby('Magasin')['Montant'].sum().reset_index()

# Créer le graphique en secteurs avec Altair
chart = alt.Chart(sales_by_store).mark_arc().encode(
    theta="Montant:Q",
    color="Magasin:N"
).properties(
    title="Répartition des ventes par magasin"
)

# Afficher le graphique sur Streamlit
st.altair_chart(chart, use_container_width=True)
