import pandas as pd
import numpy as np
import missingno as msno
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
import plotly.express as px
from geopy.geocoders import Nominatim

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
        <p>Developer : Delaunay Valentin</p>
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

st.header('I. Why this project ?')
st.write('In the current context, the "Fuel prices in France - Instant flow dataset" holds significant relevance due to the global challenges surrounding energy consumption, environmental sustainability, and economic stability.')
st.write('With increasing fuel demand, particularly in the transportation sector, tracking and analyzing fuel prices in France is crucial. It provides essential insights into the economic impact of rising fuel costs on consumers, businesses, and the overall economy.')
st.write('Furthermore, as countries seek to transition towards cleaner and more sustainable energy sources, understanding the fluctuations in fuel prices can inform policies aimed at reducing carbon emissions and promoting alternative energy solutions. The dataset is updated daily and contains information on fuel prices in France.')

st.header('II. Short presentation of data')

presentation_selection=st.selectbox('Select the type of information you need:', ['The name of the columns', 'The first 10 lines', 'The name of the columns with their type', 'The desciption of the dataset', 'The shape of the dataset', 'The number of missing values and the number of duplicates'])
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
elif (presentation_selection=='The first 10 lines'):
    st.write('The first 10 lines of the dataset are:')
    st.write(instant_fuel.head(10))
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
    msno.bar(instant_fuel)
    plt.savefig('missingno_bar_chart.png')
    image_path = 'missingno_bar_chart.png'
    image_width = 900
    image_height = 450
    image = Image.open('missingno_bar_chart.png')
    image = image.resize((image_width, image_height), Image.ANTIALIAS)
    st.image(image, caption='Missing Values Bar Chart', use_column_width=False)
    st.write('The number of duplicates in the dataset is: ' + str(instant_fuel.duplicated().sum()))

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
instant_fuel['prix_valeur']=instant_fuel['prix_valeur'].round(2)
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

median_prices = instant_fuel.groupby('prix_nom')['prix_valeur'].median()
def categorize_price(price, median, percentile_33_high, percentile_33_low):
    if price >= percentile_33_high:
        return 'cher'
    elif price <= percentile_33_low:
        return 'bas'
    else:
        return 'moyen'
percentile_33_high = instant_fuel.groupby('prix_nom')['prix_valeur'].quantile(0.67)
percentile_33_low = instant_fuel.groupby('prix_nom')['prix_valeur'].quantile(0.33)
instant_fuel['prix_categorie'] = instant_fuel.apply(lambda row: categorize_price(row['prix_valeur'], median_prices[row['prix_nom']], percentile_33_high[row['prix_nom']], percentile_33_low[row['prix_nom']]), axis=1)

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


st.write(median_prices)
st.write(instant_fuel.head(30))

st.header('III. Data Visualisation')

def geocode_address(address):
    geolocator = Nominatim(user_agent="geocoder")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None

search_input = st.text_input("Search for a location")

colors = {
    'cher': 'red',
    'moyen': 'blue',
    'pas cher': 'green',
}

m = folium.Map(location=[46.6031, 2.3522], zoom_start=5)
for i, row in instant_fuel.iterrows():
    station_category = row['station_category']
    if station_category in colors:
        color = colors[station_category]
    else:
        color = 'gray'
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
    ).add_to(m)

if search_input:
    search_location = geocode_address(search_input)
    if search_location:
        m.location = search_location
    else:
        st.warning("Location not found. Displaying default view.")

st.components.v1.html(m._repr_html_(), height=600)

selected_fuel_types = st.selectbox('Select Fuel Types:', instant_fuel['prix_nom'].unique())
filtered_data = instant_fuel[instant_fuel['prix_nom'] == selected_fuel_types]
mean_prices_by_date = filtered_data.groupby('date')['prix_valeur'].mean().reset_index()
fig = px.line(mean_prices_by_date, x='date', y='prix_valeur', title=f'Variation of Mean Price of {selected_fuel_types} in France')
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Mean Price')
fig.update_layout(
    autosize=False,
    width=1000,
    height=600
)
st.plotly_chart(fig)

st.header('IV. Conclusion')

#instant_fuel['services_service'] = instant_fuel['services_service'].str.split('//')
#instant_fuel = instant_fuel.explode('services_service')
#instant_fuel.reset_index(drop=True, inplace=True)