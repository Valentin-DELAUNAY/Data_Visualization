# PS: Please, let the time for the streamlit page to display everything. Sometimes, it will take time (due to the specification of the computer, ...)
Rarely, the page wont display everything or a part of the dataset. In this case, please refresh the page.

# Data Visualisation project, Fuel prices in France - Instant flow






## Description du Projet :
In this project, I use a dataset entitled "Fuel prices in France - Instant flow" from the French government site, Data.gouv.fr.
This dataset can be consulted by following this link: https://www.data.gouv.fr/fr/datasets/prix-des-carburants-en-france-flux-instantane/.
These data are extracted from the “Fuel Prices” information system and are linked to the fuel sales points listed on the Fuel Prices website, in accordance with a ministerial decree dated December 12, 2006.
 
The data made available in this dataset includes several categories of essential information:

    - General information about the point of sale: This includes details such as the address of the point of sale, geographical coordinates, opening hours, and the services offered by each gas station.

    - Prices and Information System Information: You can access current fuel prices, as well as other information contained in the information system. This data is crucial for motorists and businesses that rely on fuel prices.

    - Fuel stock outs: The dataset notifies you of times when a point of sale is experiencing fuel stock outs, which can be useful for users looking for fuel.

    - Permanent or temporary closures of points of sale: You can also follow the closures, whether temporary or permanent, of the listed service stations.
 
As explained in the title, the data is instantaneous (updated every 10 minutes).
 
The project is divided into 5 parts: the introduction, a short presentation of the initial dataset, the data cleaning (in the python code - not pressented in the streamlit page), the data vizualisation and a conclusion
 
## Read me- table of content:
 
    I] Use and installation
    II] Screenshots of the different stages of the streamlit page
 
## I] Use and installation
You can access to the project by different ways: by using the python file or by the link: https://datavisualization-instant-fuel.streamlit.app/
 
If you want the access it from the python file:

- Open anaconda

![Alt text](image.png)

- Create a new virtual environment

![Alt text](image-1.png)

- Open the terminal

![Alt text](image-2.png)

- Make sure you installed all the librairies needed : pip install streamlit pandas numpy matplotlib Pillow seaborn folium plotly geopy
                                                      pip install folium-plugins

- Launch VSCODE and also install all the librairies needed (in the VSCODE terminal)

![Alt text](image-4.png)

- Run the python script of VSCODE

![Alt text](image-3.png)

- Copy the terminal result on the environment terminal (anaconda): streamlit run -...

![Alt text](image-5.png)
 
## II] Explanation of the different stages of the streamlit page
 
### Introduction:
I tried to explain why I choose this project and the dataset was the most relevant and interesting
 
### A short présentation of the initial dataset
I give the possibility to have a quick overview of the given dataset before any modification
Here are the possibilities:
![Alt text](image-6.png)
 
### A data cleaning (code)
Some of the given data was useless for my project, that's why I delete them.
I also add some usefull columns in order to have a better visualization.
Moreover, the column 'horaires' was unusable (always changing)

### The data vizualisation
You have the possibility to get some simple and usefull vizualisation. Among them:
![Alt text](image-7.png)

### Finaly, the conclusion
It's a quick overview of the results.
I have also added ideas that could explain the drop in prices but also a possible increase in the days to come.