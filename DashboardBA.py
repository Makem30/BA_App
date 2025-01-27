import streamlit as st
import pandas as pd
import altair as alt

with st.sidebar:
    st.title('DASHBOARD')
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
        padding: 20px;
        border-radius: 5px;
        color: black; /* Texte blanc */
        text-align: center; /* Centrer le texte */
    }
    .metric-label {
        font-size: 10px;
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
        f'<div class="metric-container"><div class="metric-label">total_ventes</div><div class="metric-value">{total_ventes:.2f}€</div></div>',
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

# import streamlit as st
# import pandas as pd
# import altair as alt


# # Charger les données
# data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

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
col1, col2 = st.columns(2)
with col1:
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

with col2:
    # Grouper les données par magasin et calculer les ventes totales et le nombre de transactions
    store_sales = data.groupby('Magasin').agg(
        Total_ventes=('Montant', 'sum'),
        Nb_transactions=('Quantite', 'nunique')
    ).reset_index()
    
    # Afficher le tableau sur Streamlit
    st.table(store_sales)
#-----------------------------------------------------------------------
# Liste des catégories de produits uniques
categories = data['Categorie_Produit'].unique()

# Sélection de la catégorie sur la sidebar
selected_category = st.sidebar.selectbox('Sélectionnez une catégorie de produit', categories)

# Filtrer les données pour la catégorie sélectionnée
filtered_data = data[data['Categorie_Produit'] == selected_category]

# Grouper les données par produit et calculer la quantité vendue
product_sales = filtered_data.groupby('Categorie_Produit')['Quantite'].sum().reset_index()

# Créer l'histogramme avec Altair
chart = alt.Chart(product_sales).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Quantite:Q'
).properties(
    title=f"Quantité vendue par produit pour la catégorie {selected_category}",
    width=800,
    height=400
)

# Afficher le graphique sur Streamlit
st.altair_chart(chart, use_container_width=True)
#----------------------------------------------------------------------------------------
# Liste des magasins uniques
magasins = data['Magasin'].unique()

# Sélection des magasins sur la sidebar
selected_magasins = st.sidebar.multiselect('Sélectionnez un ou plusieurs magasins', magasins, default=magasins)

# Filtrer les données pour les magasins sélectionnés
filtered_data = data[data['Magasin'].isin(selected_magasins)]

# Grouper les données par catégorie et magasin, puis calculer le total des ventes
category_sales = filtered_data.groupby(['Categorie_Produit', 'Magasin'])['Montant'].sum().reset_index()

# Créer le graphique empilé avec Altair
chart = alt.Chart(category_sales).mark_bar().encode(
    x='Categorie_Produit:N',
    y='Montant:Q',
    color='Magasin:N'
).properties(
    title='Montant des ventes par catégorie et magasin',
    width=800,
    height=400
)

# Afficher le graphique sur Streamlit
st.altair_chart(chart, use_container_width=True)
#-----------------------------------------------------------------------------------
import streamlit as st
import pandas as pd

# Charger les données
data = pd.read_csv('data_dashboard_large - data_dashboard_large.csv')

# Liste des catégories de produits uniques
categories = data['Categorie_Produit'].unique().tolist()  # Convertir en liste

# Sélection de la catégorie sur la sidebar
selected_category = st.radio('Sélectionnez une catégorie de produit', categories)

# Filtrer les données pour la catégorie sélectionnée
filtered_data = data[data['Categorie_Produit'] == selected_category]

# Grouper par produit, puis calculer la quantité vendue
# Remplacez 'Quantity' et 'Product' par les noms de colonnes corrects si nécessaire
product_sales = filtered_data.groupby('Montant')['Quantite'].sum().reset_index()

# Trier par quantité vendue et obtenir le top 5
top_products = product_sales.sort_values('Quantite', ascending=False).head(5)

# Afficher le tableau sur Streamlit
st.table(top_products)
#-------------------------------------------------------------------------------------------
# col1, col2 = st.columns(2)
col1, col2 = st.columns([1,0.7],gap="large")
# Calculer le nombre de transactions par mode de paiement
with col1:
    payment_counts = data["Mode_Paiement"].value_counts().reset_index()
    payment_counts.columns = ["Mode_Paiement", "Montant"]  # Renommer les colonnes
    
    # Créer le graphique en secteurs avec Altair
    chart = alt.Chart(payment_counts).mark_arc().encode(
        theta="Montant:Q",  # Angle des secteurs basé sur le nombre de transactions
        color="Mode_Paiement:N"  # Couleur des secteurs basé sur le mode de paiement
    ).properties(
        title="Répartition des transactions par mode de paiement"
    )
    
    # Afficher le graphique sur Streamlit
    st.altair_chart(chart, use_container_width=True)
#---------------------------------------------------------------------------------
# Trouver le mode de paiement le plus utilisé
with col2:
    # most_used_payment = data["Mode_Paiement"].mode()[0]
    
    # # Afficher le KPI
    # st.metric(label="Mode de paiement le plus utilisé", value=most_used_payment)

   # Trouver le mode de paiement le plus utilisé
    most_used_payment = data["Mode_Paiement"].mode()[0]
    
    # Définir le style CSS pour le rectangle et le centrage
    st.markdown(
        """
        <style>
        .kpi-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center; /* Centre le texte à l'intérieur du rectangle */
            margin: 0 auto; /* Centre le rectangle horizontalement */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Afficher le KPI dans le rectangle
    with st.container():  # Crée un conteneur pour le rectangle
        st.markdown('<div class="kpi-container">', unsafe_allow_html=True)
        st.metric(label="Mode de paiement le plus utilisé", value=most_used_payment)
        st.markdown('</div>', unsafe_allow_html=True)

#-----------------------------------------------------------------------------------
# Calculer la moyenne de satisfaction par magasin et catégorie
satisfaction_mean = data.groupby(["Magasin", "Categorie_Produit"])["Satisfaction_Client"].mean().reset_index()

# Créer le graphique à barres avec Altair
chart = alt.Chart(satisfaction_mean).mark_bar().encode(
    x="Categorie_Produit:N",  # Catégorie sur l'axe des x
    y="mean(Satisfaction_Client):Q",  # Moyenne de satisfaction sur l'axe des y
    color="Magasin:N"  # Couleur des barres en fonction du magasin
).properties(
    title="Moyenne de satisfaction par magasin et catégorie de produit",
    width=800,  # Ajuster la largeur selon vos besoins
    height=400  # Ajuster la hauteur selon vos besoins
)

# Afficher le graphique sur Streamlit
st.altair_chart(chart, use_container_width=True)
#-------------------------------------------------------------------------------------------
# Calculer la distribution des scores de satisfaction
satisfaction_distribution = data["Satisfaction_Client"].value_counts().sort_index()

# Créer un DataFrame pour le tableau
satisfaction_df = pd.DataFrame(
    {"Score de satisfaction": satisfaction_distribution.index, "Nombre de clients": satisfaction_distribution.values}
)

# Afficher le tableau sur Streamlit
st.table(satisfaction_df)
