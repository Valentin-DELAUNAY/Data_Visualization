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

#Creation of the sidebar:
st.sidebar.title('Menu')
st.sidebar.subheader('Data Visualisation project')
st.sidebar.markdown('   ')
st.sidebar.markdown('I. Why this project ?')
st.sidebar.markdown('II. Short presentation of data')
st.sidebar.markdown('III. Data Visualisation')
st.sidebar.markdown('IV. Conclusion')
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

#Presentation of the project (introduction):
st.header('I. Why this project ?')
st.write('In the current context, the "Fuel prices in France - Instant flow dataset" holds significant relevance due to the global challenges surrounding energy consumption, environmental sustainability, and economic stability.')
st.write('With increasing fuel demand, particularly in the transportation sector, tracking and analyzing fuel prices in France is crucial. It provides essential insights into the economic impact of rising fuel costs on consumers, businesses, and the overall economy.')
st.write('Furthermore, as countries seek to transition towards cleaner and more sustainable energy sources, understanding the fluctuations in fuel prices can inform policies aimed at reducing carbon emissions and promoting alternative energy solutions. The dataset is updated daily and contains information on fuel prices in France.')

st.header('II. Short presentation of data')

presentation_selection=st.selectbox('Select the type of information you need:', ['The name of the columns', 'The first 20 lines', 'The name of the columns with their type', 'The desciption of the dataset', 'The shape of the dataset', 'The number of missing values and the number of duplicates'])
if (presentation_selection=='The name of the columns'):
    st.write('The dataset contains the following columns:')
    column_names = instant_fuel.columns.tolist()
    half_length = len(column_names) // 2
    column_names_left = column_names[:half_length]
    column_names_right = column_names[half_length:]
    left_table = pd.DataFrame({'Column Name': column_names_left}).to_markdown(index=False)
    right_table = pd.DataFrame({'Column Name': column_names_right}).to_markdown(index=False)
    columns = st.columns(2)
    with columns[0]:
        st.markdown(left_table)
    with columns[1]:
        st.markdown(right_table)
    st.write(' ')
    st.write('The dataset have ' + str(instant_fuel.shape[1]) +' columns in total.')
elif (presentation_selection=='The first 20 lines'):
    st.write('The first 20 lines of the dataset are:')
    st.write(instant_fuel.head(20))
elif (presentation_selection=='The name of the columns with their type'):
    st.write('The dataset contains the following columns with their type:')
    column_info = instant_fuel.dtypes
    num_columns = len(column_info)
    third_length = num_columns // 3
    column_info_part1 = column_info.iloc[:third_length]
    column_info_part2 = column_info.iloc[third_length:2 * third_length]
    column_info_part3 = column_info.iloc[2 * third_length:]
    column_info_df_part1 = pd.DataFrame({'Column Name': column_info_part1.index, 'Data Type': column_info_part1.values})
    column_info_df_part2 = pd.DataFrame({'Column Name': column_info_part2.index, 'Data Type': column_info_part2.values})
    column_info_df_part3 = pd.DataFrame({'Column Name': column_info_part3.index, 'Data Type': column_info_part3.values})
    columns = st.columns(3)
    columns[0].dataframe(column_info_df_part1.set_index('Column Name'))
    columns[1].dataframe(column_info_df_part2.set_index('Column Name'))
    columns[2].dataframe(column_info_df_part3.set_index('Column Name'))
    st.write('The dataset has ' + str(num_columns) + ' columns in total.')
elif (presentation_selection=='The desciption of the dataset'):
    st.write('Some information about the dataset:')
    st.write(instant_fuel.describe())
    st.write('The dataset have ' + str(instant_fuel.shape[1]) +' columns in total.')
elif (presentation_selection=='The shape of the dataset'):
    st.write('The dataset have ' + str(instant_fuel.shape[0]) +' rows and ' + str(instant_fuel.shape[1]) +' columns in total.')
elif (presentation_selection=='The number of missing values and the number of duplicates'):
    st.write('The number of missing values in the dataset is:')
    st.bar_chart(instant_fuel.isnull().sum())
    st.write('There is ' + str(instant_fuel.duplicated().sum()) + ' values duplicated in the dataset.')

#Preparation of the dataset:
instant_fuel['date'] = pd.to_datetime(instant_fuel['date']).dt.date
for x in instant_fuel.columns:
    if (instant_fuel[x].isnull().sum() > 0):
        instant_fuel = instant_fuel.dropna(subset=[x])
instant_fuel['cp']=instant_fuel['cp'].round(2)
instant_fuel['pop']=instant_fuel['pop'].astype(str)
instant_fuel['adresse']=instant_fuel['adresse'].astype(str)
instant_fuel['ville']=instant_fuel['ville'].astype(str)
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

st.header('III. Data Visualisation')

st.subheader("Discover the data by some plots:")
plot_data=st.selectbox("Select the type of plot you want to see", ["The distribution of the fuel prices (France, Region, Department, City)", "Mean price of each type of fuel (France, Region, Departement, City)", "Number of stations offering each type of fuel (France, Region, Department, City)", "Number of 24h/24h stations (France, Region, Department, City)", "Top 10 of the lowest price stations (France, Region, Department, City)"])
if plot_data == "The distribution of the fuel prices (France, Region, Department, City)":
    st.subheader("- The distribution of fuel prices in France is as follows:")
    selected_fuel_france = st.selectbox("Select Fuel Type", instant_fuel["prix_nom"].unique(), key="fuel_select_france")
    filtered_data_france = instant_fuel[instant_fuel["prix_nom"] == selected_fuel_france]
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data_france["prix_valeur"], bins=20, edgecolor='k')
    plt.xlabel("Fuel Price")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {selected_fuel_france} prices in France")
    st.pyplot(plt)
    st.write('Number of stations giving ' + selected_fuel_france + ' in France: ' + str(len(filtered_data_france)))
    st.write(' ')
    st.write(' ')

    st.subheader("- The distribution of fuel prices for regions is as follows:")
    selected_reg = st.selectbox("Select region", instant_fuel["reg_name"].unique(), key="region_select")
    selected_fuel = st.selectbox("Select Fuel Type", instant_fuel["prix_nom"].unique(), key="fuel_select_region")
    filtered_data = instant_fuel[(instant_fuel["reg_name"] == selected_reg) & (instant_fuel["prix_nom"] == selected_fuel)]
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data["prix_valeur"], bins=20, edgecolor='k')
    plt.xlabel("Fuel Price")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {selected_fuel} prices in {selected_reg}")
    st.pyplot(plt)
    st.write('Number of stations in ' + selected_reg + ' giving ' + selected_fuel + ' : ' + str(len(filtered_data)))

    st.subheader("- The distribution of fuel prices for departments is as follows:")
    selected_reg = st.selectbox("Select departments", instant_fuel["dep_name"].unique(), key="region_select_dept")
    selected_fuel = st.selectbox("Select Fuel Type", instant_fuel["prix_nom"].unique(), key="fuel_select_dept")
    filtered_data = instant_fuel[(instant_fuel["dep_name"] == selected_reg) & (instant_fuel["prix_nom"] == selected_fuel)]
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data["prix_valeur"], bins=20, edgecolor='k')
    plt.xlabel("Fuel Price")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {selected_fuel} prices in {selected_reg}")
    st.pyplot(plt)
    st.write('Number of stations in ' + selected_reg + ' giving ' + selected_fuel + ' : ' + str(len(filtered_data)))
    st.write(' ')
    st.write(' ')
    
    st.subheader("- The distribution of fuel prices for cities is as follows:")
    cities = sorted(instant_fuel["ville"].unique())
    selected_city = st.selectbox("Select a city", cities, index=cities.index("Paris"), key="city_select")
    selected_fuel = st.selectbox("Select Fuel Type", instant_fuel["prix_nom"].unique(), key="fuel_select_city")
    filtered_data = instant_fuel[(instant_fuel["ville"] == selected_city) & (instant_fuel["prix_nom"] == selected_fuel)]
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data["prix_valeur"], bins=20, edgecolor='k')
    plt.xlabel("Fuel Price")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {selected_fuel} prices in {selected_city}")
    st.pyplot(plt)
    st.write('Number of stations in ' + selected_city + ' giving ' + selected_fuel + ' : ' + str(len(filtered_data)))
elif (plot_data=="Mean price of each type of fuel (France, Region, Departement, City)"):
    st.subheader("- Mean price of a particular type of fuel in France:")
    plt.figure(figsize=(10, 6))
    plt.bar(instant_fuel["prix_nom"].unique(), instant_fuel.groupby("prix_nom")["prix_valeur"].mean())
    plt.xlabel("Fuel Type")
    plt.ylabel("Mean Price")
    plt.title("Mean Price of a Particular Type of Fuel in France")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Mean price of each type of fuel in a region:")
    selected_reg = st.selectbox("Select region", instant_fuel["reg_name"].unique())
    filtered_data = instant_fuel[instant_fuel["reg_name"] == selected_reg]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['prix_nom'].unique(), filtered_data.groupby("prix_nom")["prix_valeur"].mean())
    plt.xlabel("Fuel Type")
    plt.ylabel("Mean Price")
    plt.title(f"Mean Price of Each Type of Fuel in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Mean price of each type of fuel in a department:")
    selected_reg = st.selectbox("Select department", instant_fuel["dep_name"].unique())
    filtered_data = instant_fuel[instant_fuel["dep_name"] == selected_reg]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['prix_nom'].unique(), filtered_data.groupby("prix_nom")["prix_valeur"].mean())
    plt.xlabel("Fuel Type")
    plt.ylabel("Mean Price")
    plt.title(f"Mean Price of Each Type of Fuel in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Mean price of each type of fuel in a city:")
    cities = sorted(instant_fuel["ville"].unique())
    selected_city = st.selectbox("Select a city", cities, index=cities.index("Paris"), key="city_select")
    filtered_data = instant_fuel[instant_fuel["ville"] == selected_city]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['prix_nom'].unique(), filtered_data.groupby("prix_nom")["prix_valeur"].mean())
    plt.xlabel("Fuel Type")
    plt.ylabel("Mean Price")
    plt.title(f"Mean Price of Each Type of Fuel in {selected_city}")
    st.pyplot(plt)
elif (plot_data=="Number of stations offering each type of fuel (France, Region, Department, City)"):
    st.subheader("- Number of stations offering fuel in France:")
    plt.figure(figsize=(10, 6))
    plt.bar(instant_fuel["prix_nom"].unique(), instant_fuel["prix_nom"].value_counts())
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Stations")
    plt.title("Number of Stations Offering Fuel in France")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Number of stations offering fuel in a region:")
    selected_reg = st.selectbox("Select region", instant_fuel["reg_name"].unique())
    filtered_data = instant_fuel[instant_fuel["reg_name"] == selected_reg]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['prix_nom'].unique(), filtered_data['prix_nom'].value_counts())
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Stations")
    plt.title(f"Number of Stations Offering Fuel in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Number of stations offering fuel in a department:")
    selected_reg = st.selectbox("Select department", instant_fuel["dep_name"].unique())
    filtered_data = instant_fuel[instant_fuel["dep_name"] == selected_reg]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['prix_nom'].unique(), filtered_data['prix_nom'].value_counts())
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Stations")
    plt.title(f"Number of Stations Offering Fuel in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Number of stations offering fuel in a city:")
    cities = sorted(instant_fuel["ville"].unique())
    selected_city = st.selectbox("Select a city", cities, index=cities.index("Paris"), key="city_select")
    filtered_data = instant_fuel[instant_fuel["ville"] == selected_city]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['prix_nom'].unique(), filtered_data['prix_nom'].value_counts())
    plt.xlabel("Fuel Type")
    plt.ylabel("Number of Stations")
    plt.title(f"Number of Stations Offering Fuel in {selected_city}")
    st.pyplot(plt)
elif (plot_data=="Number of 24h/24h stations (France, Region, Department, City)"):
    mapping = {0: "non", 1: "oui"}
    instant_fuel["horaires_automate_24_24"] = instant_fuel["horaires_automate_24_24"].map(mapping)
    st.subheader("- Number of 24h/24h stations in France:")
    plt.figure(figsize=(10, 6))
    plt.bar(instant_fuel["horaires_automate_24_24"].unique(), instant_fuel["horaires_automate_24_24"].value_counts())
    plt.xlabel("24h/24h")
    plt.ylabel("Number of Stations")
    plt.title("Number of 24h/24h Stations in France")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Number of 24h/24h stations in a region:")
    selected_reg = st.selectbox("Select region", instant_fuel["reg_name"].unique())
    filtered_data = instant_fuel[instant_fuel["reg_name"] == selected_reg]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['horaires_automate_24_24'].unique(), filtered_data['horaires_automate_24_24'].value_counts())
    plt.xlabel("24h/24h")
    plt.ylabel("Number of Stations")
    plt.title(f"Number of 24h/24h Stations in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Number of 24h/24h stations in a department:")
    selected_reg = st.selectbox("Select department", instant_fuel["dep_name"].unique())
    filtered_data = instant_fuel[instant_fuel["dep_name"] == selected_reg]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['horaires_automate_24_24'].unique(), filtered_data['horaires_automate_24_24'].value_counts())
    plt.xlabel("24h/24h")
    plt.ylabel("Number of Stations")
    plt.title(f"Number of 24h/24h Stations in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    st.write(' ')

    st.subheader("- Number of 24h/24h stations in a city:")
    cities = sorted(instant_fuel["ville"].unique())
    selected_city = st.selectbox("Select a city", cities, index=cities.index("Paris"), key="city_select")
    filtered_data = instant_fuel[instant_fuel["ville"] == selected_city]
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['horaires_automate_24_24'].unique(), filtered_data['horaires_automate_24_24'].value_counts())
    plt.xlabel("24h/24h")
    plt.ylabel("Number of Stations")
    plt.title(f"Number of 24h/24h Stations in {selected_city}")
    st.pyplot(plt)
elif (plot_data=="Top 10 of the lowest price stations (France, Region, Department, City)"):
    fuel_types = instant_fuel["prix_nom"].unique()
    selected_fuel = st.selectbox("Select Fuel Type for all the plots:", fuel_types)
    filtered_data = instant_fuel[instant_fuel["prix_nom"] == selected_fuel]
    st.write(' ')
    top_10_lowest_prices = filtered_data.sort_values(by="prix_valeur").head(10)
    st.subheader("- Top 10 of the lowest price stations in France:")
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_lowest_prices["id"].astype(str), top_10_lowest_prices["prix_valeur"])
    plt.xlabel("Station ID")
    plt.ylabel("Lowest Price")
    plt.title("Top 10 of the lowest price stations in France")
    st.pyplot(plt)
    st.write(' ')
    for index, row in top_10_lowest_prices.iterrows():
        st.write(f"Station informations about {row['id']}: {row['adresse']}, {row['ville']} ({row['cp']})")
        st.write(f"Price of {row['prix_nom']}: {row['prix_valeur']} €")
        st.write(' ')
    st.write(' ')

    st.subheader("- Top 10 of the lowest price stations in a region:")
    selected_reg = st.selectbox("Select region", instant_fuel["reg_name"].unique())
    filtered_data = instant_fuel[(instant_fuel["reg_name"] == selected_reg) & (instant_fuel["prix_nom"] == selected_fuel)]
    top_10_lowest_prices = filtered_data.sort_values(by="prix_valeur").head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_lowest_prices["id"].astype(str), top_10_lowest_prices["prix_valeur"])
    plt.xlabel("Station ID")
    plt.ylabel("Lowest Price")
    plt.title(f"Top 10 of the lowest price stations in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    for index, row in top_10_lowest_prices.iterrows():
        st.write(f"Station informations about {row['id']}: {row['adresse']}, {row['ville']} ({row['cp']})")
        st.write(f"Price of {row['prix_nom']}: {row['prix_valeur']} €")
        st.write(' ')
    st.write(' ')
    
    st.subheader("- Top 10 of the lowest price stations in a department:")
    selected_reg = st.selectbox("Select department", instant_fuel["dep_name"].unique())
    filtered_data = instant_fuel[(instant_fuel["dep_name"] == selected_reg) & (instant_fuel["prix_nom"] == selected_fuel)]
    top_10_lowest_prices = filtered_data.sort_values(by="prix_valeur").head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_lowest_prices["id"].astype(str), top_10_lowest_prices["prix_valeur"])
    plt.xlabel("Station ID")
    plt.ylabel("Lowest Price")
    plt.title(f"Top 10 of the lowest price stations in {selected_reg}")
    st.pyplot(plt)
    st.write(' ')
    for index, row in top_10_lowest_prices.iterrows():
        st.write(f"Station informations about {row['id']}: {row['adresse']}, {row['ville']} ({row['cp']})")
        st.write(f"Price of {row['prix_nom']}: {row['prix_valeur']} €")
        st.write(' ')
    st.write(' ')
    
    st.subheader("- Top 10 of the lowest price stations in a city:")
    cities = sorted(instant_fuel["ville"].unique())
    selected_city = st.selectbox("Select a city", cities, index=cities.index("Paris"), key="city_select")
    filtered_data = instant_fuel[(instant_fuel["ville"] == selected_city) & (instant_fuel["prix_nom"] == selected_fuel)]
    top_10_lowest_prices = filtered_data.sort_values(by="prix_valeur").head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_10_lowest_prices["id"].astype(str), top_10_lowest_prices["prix_valeur"])
    plt.xlabel("Station ID")
    plt.ylabel("Lowest Price")
    plt.title(f"Top 10 of the lowest price stations in {selected_city}")
    st.pyplot(plt)
    st.write(' ')
    for index, row in top_10_lowest_prices.iterrows():
        st.write(f"Station informations about {row['id']}: {row['adresse']}, {row['ville']} ({row['cp']})")
        st.write(f"Price of {row['prix_nom']}: {row['prix_valeur']} €")
        st.write(' ')
    st.write(' ')

st.write(' ')
st.subheader('Discover the data by the map:')

#Creation of the map
initial_location = [46.6031, 2.3522]
initial_zoom = 5

def update_map(data, location, zoom, add_marker=False):
    m = folium.Map(location=location, zoom_start=zoom)
    colors = {
        'cher': 'red',
        'moyen': 'orange',
        'pas cher': 'green',
    }
    for _, row in data.iterrows():
        station_category = row['station_category']
        color = colors.get(station_category, 'gray')

        marker = folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
        )
        fuel_info = ""
        station_rows = instant_fuel[instant_fuel['id'] == row['id']]
        for _, station_row in station_rows.iterrows():
            prix_nom = station_row['prix_nom']
            prix_valeur = station_row['prix_valeur']
            prix_categorie = station_row['prix_categorie']
            fuel_info += f"<span style='color:{colors.get(prix_categorie, 'green')}'>●</span> {prix_nom}: {prix_valeur} <br>"
        popup_content = f"""<div style='width: 200px; height: 150px;'>
                            Adresse: {row['adresse']}, {row['ville']} ({row['cp']}) <br><br>
                            Carburants: <br>{fuel_info} <br>
                            Automate 24/24: {'oui' if row['horaires_automate_24_24'] == 1 else 'non'} <br>
                            </div>"""
        folium.Popup(popup_content).add_to(marker)
        marker.add_to(m)
    
    if add_marker:
        folium.Marker(
            location=location,
            popup="Search Location",
            icon=folium.Icon(color='purple')
        ).add_to(m)
    
    legend_html = """
    <div style="position: fixed; bottom: 50px; left: 50px; z-index:1000; background-color: white; padding: 10px; border: 2px solid gray;">
        <p><strong>Type of station</strong></p>
        <p><i class="fa fa-circle" style="color: red;"></i> cher</p>
        <p><i class="fa fa-circle" style="color: orange;"></i> moyen</p>
        <p><i class="fa fa-circle" style="color: green;"></i> pas cher</p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    
    return m

with st.form(key='search_form'):
    search_input = st.text_input("Search for a location:")
    search_button = st.form_submit_button("Search")

st.write(' ')
st.subheader('Filter your research:')
st.write(' ')
fuel_checkboxes = {}
st.write('Select the type of fuel you want to see: (initialy Gazole)')
col1, col2, col3, col4, col5, col6 = st.columns(6)
for x, col in zip(instant_fuel['prix_nom'].unique(), [col1, col2, col3, col4, col5, col6]):
    checkbox_key = f"checkbox_{x}"
    initial_value = True if x == 'Gazole' else False
    fuel_checkboxes[x] = col.checkbox(x, key=checkbox_key, value=initial_value)
selected_fuels = [fuel_type for fuel_type, selected in fuel_checkboxes.items() if selected]
st.write(' ')

st.write('Select the services needed (if you need one):')
only_services = instant_fuel['services_service'].str.split('//')
only_services = only_services.explode('services_service')
only_services.reset_index(drop=True, inplace=True)

unique_services = only_services.unique()

num_columns_per_row = 3

num_rows = len(unique_services) // num_columns_per_row
if len(unique_services) % num_columns_per_row != 0:
    num_rows += 1
services_checkboxes = {}

for i in range(num_rows):
    row = st.columns(num_columns_per_row)
    for j in range(num_columns_per_row):
        index = i * num_columns_per_row + j
        if index < len(unique_services):
            service = unique_services[index]
            checkbox_key = f"checkbox_{service}"
            services_checkboxes[service] = row[j].checkbox(service, key=checkbox_key)

selected_services = [service for service, selected in services_checkboxes.items() if selected]
zoom_level = initial_zoom
add_marker = False
if search_input:
    geolocator = Nominatim(user_agent="geocoder")
    location = geolocator.geocode(search_input)
    if location:
        search_location = [location.latitude, location.longitude]
        zoom_level = 12
        add_marker = True
    else:
        search_location = initial_location
else:
    search_location = initial_location

selected_fuels = [fuel_type for fuel_type, selected in fuel_checkboxes.items() if selected]
filtered_data = instant_fuel[instant_fuel['prix_nom'].isin(selected_fuels)]
filtered_services = [service for service, selected in services_checkboxes.items() if selected]
filtered_data = filtered_data[filtered_data['services_service'].str.contains('|'.join(filtered_services))]

if search_button:
    geolocator = Nominatim(user_agent="geocoder")
    location = geolocator.geocode(search_input)
    
    if location:
        search_location = [location.latitude, location.longitude]
        zoom_level = 12
        add_marker = True
        st.success("Location found. Updating the map.")
    else:
        st.warning("Location not found. Displaying default view.")

filtered_map = update_map(filtered_data, search_location, zoom_level, add_marker)
st.components.v1.html(filtered_map._repr_html_(), height=600)

#Plot of the mean price of the fuel selected:
instant_fuel['date'] = pd.to_datetime(instant_fuel['date'])
instant_fuel = instant_fuel.sort_values(by='date', ascending=True)
instant_fuel['price_change'] = instant_fuel['prix_valeur'].diff()

selected_fuel_types = st.selectbox('Select Fuel Types:', instant_fuel['prix_nom'].unique())
filtered_data_0 = instant_fuel[instant_fuel['prix_nom'] == selected_fuel_types]
mean_price = filtered_data_0['prix_valeur'].mean()
mean_price_change = filtered_data_0['price_change'].iloc[-1]
mean_price_30d = filtered_data_0['prix_valeur'].iloc[-30:].mean()
mean_price_120d = filtered_data_0['prix_valeur'].iloc[-120:].mean()
mean_price_360d = filtered_data_0['prix_valeur'].iloc[-360:].mean()
mean_variation= mean_price_change / mean_price * 100
median_price = filtered_data_0['prix_valeur'].median()
median_price_change = filtered_data_0['price_change'].iloc[-1]
median_price_30d = filtered_data_0['price_change'].iloc[-30:].median()
median_price_120d = filtered_data_0['price_change'].iloc[-120:].median()
median_price_360d = filtered_data_0['price_change'].iloc[-360:].median()
median_variation = median_price_change / median_price * 100

equal = "https://cdn-icons-png.flaticon.com/512/660/660520.png"
arrow_up = "https://cdn-icons-png.flaticon.com/512/7456/7456066.png"
arrow_down = "https://cdn-icons-png.flaticon.com/512/3227/3227489.png"

col1, col2 = st.columns(2)

with col1:
    st.write("<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
    st.markdown(f"**Mean price:** {mean_price:.3f} ({mean_variation:.3f}%)")
    
    if mean_price_change > 0:
        st.image(arrow_up, width=45)
    elif mean_price_change < 0:
        st.image(arrow_down, width=45)
    else:
        st.image(equal, width=45)

    col3, col4, col5 = st.columns(3)
    st.write(' ')
    with col3:
        st.markdown(f"**1 month variation:** {mean_price_30d:.3f}")
        if mean_price_30d > 0:
            st.image(arrow_up, width=45)
        elif mean_price_30d < 0:
            st.image(arrow_down, width=45)
        else:
            st.image(equal, width=45)
    with col4:
        st.markdown(f"**6 months variation:** {mean_price_120d:.3f}")
        if mean_price_120d > 0:
            st.image(arrow_up, width=45)
        elif mean_price_120d < 0:
            st.image(arrow_down, width=45)
        else:
            st.image(equal, width=45)
    with col5:
        st.markdown(f"**1 year variation:** {mean_price_360d:.3f}")
        if mean_price_360d > 0:
            st.image(arrow_up, width=45)
        elif mean_price_360d < 0:
            st.image(arrow_down, width=45)
        else:
            st.image(equal, width=45)

with col2:
    st.write("<div style='display: flex; align-items: center;'>", unsafe_allow_html=True)
    st.markdown(f"**Median price:** {median_price:.3f} ({median_variation:.3f}%)")
    if median_price_change > 0:
        st.image(arrow_up, width=45)
    elif median_price_change < 0:
        st.image(arrow_down, width=45)
    else:
        st.image(equal, width=45)
    
    col6, col7, col8 = st.columns(3)
    st.write(' ')
    with col6:
        st.markdown(f"**1 month variation:** {median_price_30d:.3f}")
        if median_price_30d > 0:
            st.image(arrow_up, width=45)
        elif median_price_30d < 0:
            st.image(arrow_down, width=45)
        else:
            st.image(equal, width=45)
    with col7:
        st.markdown(f"**6 months variation:** {median_price_120d:.3f}")
        if median_price_120d > 0:
            st.image(arrow_up, width=45)
        elif median_price_120d < 0:
            st.image(arrow_down, width=45)
        else:
            st.image(equal, width=45)
    with col8:
        st.markdown(f"**1 year variation:** {median_price_360d:.3f}")
        if median_price_360d > 0:
            st.image(arrow_up, width=45)
        elif median_price_360d < 0:
            st.image(arrow_down, width=45)
        else:
            st.image(equal, width=45)

overall_mean_price= filtered_data_0['prix_valeur'].mean()
mean_prices_by_date = filtered_data_0.groupby('date')['prix_valeur'].mean().reset_index()
overall_mean_price = filtered_data_0['prix_valeur'].mean()
fig = px.line(
    mean_prices_by_date,
    x='date',
    y='prix_valeur',
    title=f'Variation of Mean Price of {selected_fuel_types} in France (2023)',
    labels={'prix_valeur': 'Mean Price', 'date': 'Date'},
)
fig.add_hline(
    y=overall_mean_price,
    line_dash="dash",
    line_color="red",
    name=f'Overall Mean Price (2023): {overall_mean_price:.2f}',
)
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Mean Price')
fig.update_xaxes(range=["2023-01-01", instant_fuel['date'].max()])
fig.add_trace(go.Scatter(x=[], y=[], mode='markers', name='dummy', showlegend=True))
st.plotly_chart(fig)

#Last part, the conclusion:
st.header('IV. Conclusion')
st.write("In conclusion, the study of instantaneous fuel prices in France reflects a complex and fluctuating dynamic, strongly influenced by various economic, geopolitical and environmental factors. The observation that prices tend to fall thanks to the actions of large retailers selling at cost price is interesting, because it shows that competition in the fuel market can have positive repercussions on consumers' wallets.")
st.write("However, it is crucial to note that this downward price trend may be fleeting, and that several external factors can reverse this trend. Geopolitical conflicts, such as the Ukraine-Russia war and the Israel-Palestine conflict, have traditionally impacted global oil markets by causing sharp fluctuations in oil prices. Volatility in fuel prices due to these events may negate the temporary benefits of large retailers selling at cost.")
st.write("In addition, the current context is marked by a government trend towards the promotion of electric vehicles and alternative energies, with the aim of reducing dependence on fossil fuels and combating climate change. This policy could potentially result in taxes or regulations aimed at discouraging the use of gasoline or diesel vehicles, which could ultimately increase costs for motorists.")
st.write("Ultimately, the study of instantaneous fuel prices in France highlights the need for consumers to remain attentive to market fluctuations, while considering more sustainable alternatives, such as the adoption of electric vehicles, to deal with uncertainties related to fuel prices and geopolitical issues. Government policies and the actions of large retailers can play a role, but diversifying means of transport and reducing dependence on fossil fuels are crucial challenges to address in a constantly changing global context.")