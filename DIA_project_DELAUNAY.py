#Importation of the libraries:
import pandas as pd
import numpy as np
import missingno as msno
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import folium
from folium.plugins import HeatMap
import plotly.express as px
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import json
from why_this_project import page_why_project
from data_presentation import page_data_presentation
from data_visualization import page_data_visualization
from conclusion import page_conclusion

#Creation of the sidebar:
st.sidebar.title('Menu')
st.sidebar.subheader('Data Visualisation project')
st.sidebar.markdown('   ')
selected_page = st.sidebar.selectbox(
    "Select a page",
    ("Why this project", "Short presentation of data", "Data visualization", "Conclusion")
)

st.sidebar.markdown(
"""
    <br>
    <div class="conteneur">
        <p>Teacher: Mano Mathew</p>
        <div class="ma-div">
            <a href="https://www.linkedin.com/in/manomathew/" target="_blank" style="text-decoration: none; color:white">
            <div style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; display: flex; align-items: center; width: 200px; justify-content: center;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" alt="LinkedIn Logo" height="20px" style="margin-right: 10px;">
                LinkedIn
            </div>
        </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True)
st.sidebar.markdown(
"""
    <br>
    <div class="conteneur">
        <p>Developer : Valentin Delaunay</p>
        <p>Efrei Paris- Promo 2025</p>
        <p>#datavz2023efrei</p>
        <div class="ma-div">
            <a href="https://www.linkedin.com/in/valentin-delaunay-ingenieur-data/" target="_blank" style="text-decoration: none; color:white">
            <div style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; display: flex; align-items: center; width: 200px; justify-content: center;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" alt="LinkedIn Logo" height="20px" style="margin-right: 10px;">
                LinkedIn
            </div>
        </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
"""
    <br>
    <div class="conteneur">
        <div class="ma-div">
            <a href="https://github.com/Valentin-DELAUNAY" target="_blank" style="text-decoration: none; color:white">
            <div style="background-color: white; color: black; padding: 10px 20px; border-radius: 5px; display: flex; align-items: center; width: 200px; justify-content: center;">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/github.svg" alt="Github" height="20px" style="margin-right: 10px;">
                Github
            </div>
        </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

instant_fuel=pd.read_csv('https://data.economie.gouv.fr/explore/dataset/prix-carburants-fichier-instantane-test-ods-copie/download?format=csv&timezone=Europe/Berlin&use_labels_for_header=false', delimiter=';')
st.title('Data Visualisation project, Fuel prices in France - Instant flow')

if selected_page == "Why this project":
    #Modification of some type of columns:
    instant_fuel['prix_maj'] = pd.to_datetime(instant_fuel['prix_maj'], utc=True)
    instant_fuel['date'] = instant_fuel['prix_maj'].dt.date
    instant_fuel['time'] = instant_fuel['prix_maj'].dt.time
    instant_fuel['date'] = pd.to_datetime(instant_fuel['date'])
    instant_fuel['time'] = pd.to_datetime(instant_fuel['time'], format='%H:%M:%S').dt.time
    date_max=instant_fuel['date'].max()
    max_date_day = instant_fuel[instant_fuel['date'] == instant_fuel['date'].max()]
    max_time = max_date_day['time'].max()
    instant_fuel=instant_fuel.drop(columns=['prix_maj'])
    formatted_date_max = date_max.strftime('%Y-%m-%d')
    formatted_max_time = max_time.strftime('%H:%M:%S')
    st.markdown('Last update: ' + formatted_date_max + ' at ' + formatted_max_time)
    page_why_project()
elif selected_page == "Short presentation of data":
    page_data_presentation(instant_fuel)
elif selected_page == "Data visualization":
    #Modification of some type of columns:
    instant_fuel['prix_maj'] = pd.to_datetime(instant_fuel['prix_maj'], utc=True)
    instant_fuel['date'] = instant_fuel['prix_maj'].dt.date
    instant_fuel['time'] = instant_fuel['prix_maj'].dt.time
    instant_fuel['date'] = pd.to_datetime(instant_fuel['date'])
    instant_fuel['time'] = pd.to_datetime(instant_fuel['time'], format='%H:%M:%S').dt.time
    date_max=instant_fuel['date'].max()
    max_date_day = instant_fuel[instant_fuel['date'] == instant_fuel['date'].max()]
    max_time = max_date_day['time'].max()
    instant_fuel=instant_fuel.drop(columns=['prix_maj'])
    formatted_date_max = date_max.strftime('%Y-%m-%d')
    formatted_max_time = max_time.strftime('%H:%M:%S')
    st.markdown('Last update: ' + formatted_date_max + ' at ' + formatted_max_time)
    #Preparation of the dataset:
    instant_fuel['date'] = pd.to_datetime(instant_fuel['date']).dt.date
    for x in instant_fuel.columns:
        if (instant_fuel[x].isnull().sum() > 0):
            instant_fuel = instant_fuel.dropna(subset=[x])
    instant_fuel['cp']=instant_fuel['cp'].round(2)
    instant_fuel['pop']=instant_fuel['pop'].astype(str)
    instant_fuel['adresse']=instant_fuel['adresse'].astype(str)
    instant_fuel['ville']=instant_fuel['ville'].astype(str)
    #drop all the stations permently closed
    instant_fuel = instant_fuel.dropna(subset=['horaires']) 
    instant_fuel['geom']=instant_fuel['geom'].astype(str)
    instant_fuel[['latitude', 'longitude']] = instant_fuel.geom.str.split(",",expand=True)
    instant_fuel['longitude']=instant_fuel['longitude'].astype(float)
    instant_fuel['latitude']=instant_fuel['latitude'].astype(float)
    instant_fuel=instant_fuel.drop(columns=['geom'])
    instant_fuel['prix_id']=instant_fuel['prix_id'].astype(int)
    instant_fuel['prix_valeur']=instant_fuel['prix_valeur'].astype(float)
    instant_fuel['prix_nom'] = instant_fuel['prix_nom'].astype(str)
    #instant_fuel['com_arm_code']=instant_fuel['com_arm_code'].astype(int)
    instant_fuel['com_arm_name']=instant_fuel['com_arm_name'].astype(str)
    instant_fuel['epci_name']=instant_fuel['epci_name'].astype(str)
    instant_fuel['dep_code']=instant_fuel['dep_code'].replace('2A','20')
    instant_fuel['dep_code']=instant_fuel['dep_code'].replace('2B','20')
    instant_fuel['dep_code']=instant_fuel['dep_code'].astype(int)
    instant_fuel['dep_name']=instant_fuel['dep_name'].astype(str)
    instant_fuel['reg_code']=instant_fuel['reg_code'].astype(int)
    instant_fuel['reg_name']=instant_fuel['reg_name'].astype(str)
    instant_fuel['horaires_automate_24_24']=instant_fuel['horaires_automate_24_24'].astype(str)
    instant_fuel['horaires_automate_24_24']=instant_fuel['horaires_automate_24_24'].replace('Oui',1)
    instant_fuel['horaires_automate_24_24']=instant_fuel['horaires_automate_24_24'].replace('Non',0)
    instant_fuel = instant_fuel.sort_values(by='id').reset_index(drop=True)
    instant_fuel.drop(columns=['pop', 'prix_id', 'com_arm_code', 'epci_code', 'dep_code', 'horaires'], inplace=True)
    mean_prices = instant_fuel.groupby('prix_nom')['prix_valeur'].mean().reset_index()
    instant_fuel = instant_fuel.merge(mean_prices, on='prix_nom', suffixes=('', '_mean'))
    #Categorization of the fuel prices:
    def categorize_prix(row):
        if row['prix_valeur'] > (1.02 * row['prix_valeur_mean']):
            return 'cher'
        elif row['prix_valeur'] < (0.98 * row['prix_valeur_mean']):
            return 'bas'
        else:
            return 'moyen'
    instant_fuel['prix_categorie'] = instant_fuel.apply(categorize_prix, axis=1)
    instant_fuel = instant_fuel.drop(columns=['prix_valeur_mean'])
    station_categories = instant_fuel.groupby('id')['prix_categorie'].apply(list)
    def determine_station_category(price_categories):
        bas_count = price_categories.count('bas')
        moyen_count = price_categories.count('moyen')
        cher_count = price_categories.count('cher')
        
        total_categories = bas_count + moyen_count + cher_count
        
        if cher_count / total_categories > 0.33:
            return 'cher'
        elif bas_count / total_categories > 0.33:
            return 'pas cher'
        else:
            return 'moyen'
    station_categories = station_categories.apply(determine_station_category)
    station_category_mapping = station_categories.reset_index().set_index('id')['prix_categorie'].to_dict()
    instant_fuel['station_category'] = instant_fuel['id'].map(station_category_mapping)
    instant_fuel['prix_nom'].dropna(inplace=True)
    page_data_visualization(instant_fuel)
elif selected_page == "Conclusion":
    page_conclusion()