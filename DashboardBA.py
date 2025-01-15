# import streamlit as st
# import pandas as pd
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

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

#-------------------------------------------------------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
data = pd.read_csv('data_dashboard_large.csv')

# Titre du dashboard
st.title("Dashboard Interactif des Performances de l'Entreprise")

# Section Résumé
st.header("Vue d'ensemble")
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
ventes_quotidiennes = data.groupby(data['Date_Transaction'].dt.date)['Montant'].sum()
st.line_chart(ventes_quotidiennes)

# Analyse par magasin
st.header("Analyse par magasin")
ventes_par_magasin = data.groupby('Magasin')['Montant'].sum()
st.bar_chart(ventes_par_magasin)

transactions_par_magasin = data.groupby('Magasin')['ID_Client'].count()
st.bar_chart(transactions_par_magasin)

# Analyse des catégories de produits
st.header("Analyse des catégories de produits")
quantites_par_categorie = data.groupby('Categorie_Produit')['Quantite'].sum()
st.bar_chart(quantites_par_categorie)

ventes_par_categorie_magasin = data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().unstack()
st.bar_chart(ventes_par_categorie_magasin)

# Analyse des modes de paiement
st.header("Analyse des modes de paiement")
transactions_par_mode = data['Mode_Paiement'].value_counts()
st.pie_chart(transactions_par_mode)

mode_paiement_populaire = transactions_par_mode.idxmax()
st.metric("Mode de paiement le plus utilisé", mode_paiement_populaire)

# Analyse de la satisfaction client
st.header("Analyse de la satisfaction client")
satisfaction_par_magasin = data.groupby('Magasin')['Satisfaction_Client'].mean()
st.bar_chart(satisfaction_par_magasin)

satisfaction_par_categorie = data.groupby('Categorie_Produit')['Satisfaction_Client'].mean()
st.bar_chart(satisfaction_par_categorie)

# Distribution des scores de satisfaction
st.subheader("Distribution des scores de satisfaction")
satisfaction_distribution = data['Satisfaction_Client'].value_counts().sort_index()
st.bar_chart(satisfaction_distribution)

# Filtres dynamiques
st.sidebar.header("Filtres")
magasin_filtre = st.sidebar.multiselect("Sélectionnez le(s) magasin(s)", options=data['Magasin'].unique(), default=data['Magasin'].unique())
categorie_filtre = st.sidebar.multiselect("Sélectionnez la/les catégorie(s)", options=data['Categorie_Produit'].unique(), default=data['Categorie_Produit'].unique())
mode_paiement_filtre = st.sidebar.multiselect("Sélectionnez le(s) mode(s) de paiement", options=data['Mode_Paiement'].unique(), default=data['Mode_Paiement'].unique())

data_filtre = data[(data['Magasin'].isin(magasin_filtre)) & (data['Categorie_Produit'].isin(categorie_filtre)) & (data['Mode_Paiement'].isin(mode_paiement_filtre))]

# Afficher les données filtrées
st.dataframe(data_filtre)

