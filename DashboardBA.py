# import streamlit as st
# import pandas as pd
# data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Calculer le total des ventes
# total_ventes = data['Montant'].sum()

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
#-----------------------------------------------------------------------------------------
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
        st.metric(label="Satisfaction client moyenne", value=f"{satisfaction_client_moyenne:.2f} €")
        st.markdown('</div>', unsafe_allow_html=True)
with col4:
    with st.container():
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric(label="Total des ventes", value=f"{satisfaction_client_moyenne:.2f} €")
        st.markdown('</div>', unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import altair as alt

# Charger les données
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Titre du dashboard
st.title("Dashboard Interactif des Performances de l'Entreprise")

# Section Résumé
st.header("Performances")
total_ventes = data['Montant'].sum()
total_transactions = data['ID_Client'].count()
montant_moyen = data['Montant'].mean()
satisfaction_moyenne = data['Satisfaction_Client'].mean()

st.metric("Total des ventes (€)", f"{total_ventes:,.2f}")
st.metric("Nombre total de transactions", total_transactions)
st.metric("Montant moyen par transaction (€)", f"{montant_moyen:,.2f}")
st.metric("Satisfaction client moyenne", f"{satisfaction_moyenne:.2f}")

# Graphique des ventes quotidiennes
st.subheader("Ventes quotidiennes")
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])
ventes_quotidiennes = data.groupby(data['Date_Transaction'].dt.date)['Montant'].sum().reset_index()
chart_ventes_quotidiennes = alt.Chart(ventes_quotidiennes).mark_line().encode(
    x='Date_Transaction:T',
    y='Montant:Q'
).properties(
    title='Ventes quotidiennes'
)
st.altair_chart(chart_ventes_quotidiennes, use_container_width=True)

# Analyse par magasin
st.header("Analyse par magasin")
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum().reset_index()
chart_ventes_par_magasin = alt.Chart(ventes_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Montant:Q'
).properties(
    title='Ventes par magasin'
)
st.altair_chart(chart_ventes_par_magasin, use_container_width=True)

transactions_par_magasin = data.groupby('Magasin')['ID_Client'].count().reset_index()
chart_transactions_par_magasin = alt.Chart(transactions_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='ID_Client:Q'
).properties(
    title='Transactions par magasin'
)
st.altair_chart(chart_transactions_par_magasin, use_container_width=True)

# Analyse des catégories de produits
st.header("Analyse des catégories de produits")
quantites_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum().reset_index()
chart_quantites_par_categorie = alt.Chart(quantites_par_categorie).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Quantite:Q'
).properties(
    title='Quantités vendues par catégorie'
)
st.altair_chart(chart_quantites_par_categorie, use_container_width=True)

ventes_par_categorie_magasin = data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().reset_index()
chart_ventes_par_categorie_magasin = alt.Chart(ventes_par_categorie_magasin).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Montant:Q',
    color='Magasin:N'
).properties(
    title='Ventes par catégorie et magasin'
)
st.altair_chart(chart_ventes_par_categorie_magasin, use_container_width=True)

# Analyse des modes de paiement
st.header("Analyse des modes de paiement")
transactions_par_mode = data['Mode_Paiement'].value_counts().reset_index()
transactions_par_mode.columns = ['Mode_Paiement', 'Nombre']
chart_transactions_par_mode = alt.Chart(transactions_par_mode).mark_arc().encode(
    theta='Nombre:Q',
    color='Mode_Paiement:N'
).properties(
    title='Répartition des transactions par mode de paiement'
)
st.altair_chart(chart_transactions_par_mode, use_container_width=True)

mode_paiement_populaire = transactions_par_mode.iloc[0]['Mode_Paiement']
st.metric("Mode de paiement le plus utilisé", mode_paiement_populaire)

# Analyse de la satisfaction client
st.header("Analyse de la satisfaction client")
satisfaction_par_magasin = data.groupby('Magasin')['Satisfaction_Client'].mean().reset_index()
chart_satisfaction_par_magasin = alt.Chart(satisfaction_par_magasin).mark_bar().encode(
    x='Magasin:N',
    y='Satisfaction_Client:Q'
).properties(
    title='Satisfaction par magasin'
)
st.altair_chart(chart_satisfaction_par_magasin, use_container_width=True)

satisfaction_par_categorie = data.groupby('Categorie_Produit')['Satisfaction_Client'].mean().reset_index()
chart_satisfaction_par_categorie = alt.Chart(satisfaction_par_categorie).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Satisfaction_Client:Q'
).properties(
    title='Satisfaction par catégorie'
)
st.altair_chart(chart_satisfaction_par_categorie, use_container_width=True)

# Distribution des scores de satisfaction
st.subheader("Distribution des scores de satisfaction")
satisfaction_distribution = data['Satisfaction_Client'].value_counts().reset_index()
satisfaction_distribution.columns = ['Score', 'Nombre']
chart_satisfaction_distribution = alt.Chart(satisfaction_distribution).mark_bar().encode(
    x='Score:N',
    y='Nombre:Q'
).properties(
    title='Distribution des scores de satisfaction'
)
st.altair_chart(chart_satisfaction_distribution, use_container_width=True)

# Filtres dynamiques
st.sidebar.header("Filtres")
magasin_filtre = st.sidebar.multiselect("Sélectionnez le(s) magasin(s)", options=data['Magasin'].unique(), default=data['Magasin'].unique())
categorie_filtre = st.sidebar.multiselect("Sélectionnez la/les catégorie(s)", options=data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
mode_paiement_filtre = st.sidebar.multiselect("Sélectionnez le(s) mode(s) de paiement", options=data['Mode_Paiement'].unique(), default=data['Mode_Paiement'].unique())

data_filtre = data[(data['Magasin'].isin(magasin_filtre)) & (data['Categorie_Produit'].isin(categorie_filtre)) & (data['Mode_Paiement'].isin(mode_paiement_filtre))]

# Afficher les données filtrées
st.dataframe(data_filtre)

