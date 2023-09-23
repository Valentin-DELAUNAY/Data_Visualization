import pandas as pd
import xml.etree.ElementTree as ET

# Function for processing XML data
def process_xml_element(x):
    # 1) Elements uniques
    id2 = x.get("id")
    cp = x.get("cp")
    latitude = x.get("latitude")
    longitude = x.get("longitude")
    adresse = x.find("adresse").text if x.find("adresse") is not None else None
    localisation = x.get("pop")
    ville = x.find("ville").text if x.find("ville") is not None else None

    # 2) Donnees dupliquees
    essence = [x for x in x.findall("prix")]

    # Initialize the essence_dict
    essence_dict = {}
    
    # Iterate through essence list and add to essence_dict
    for e in essence:
        attrs = e.attrib
        essence_dict.update(attrs)

    # 3) Fusion des resultats
    result = {
        "id2": id2,
        "cp": cp,
        "ville": ville,
        "type_station": localisation,
        "latitude": latitude,
        "longitude": longitude,
        "adresse": adresse,
        **essence_dict  # Add all attributes from essence_dict
    }
    
    return result

# Load XML data
tree = ET.parse("C:\Valentin\M1 2023-2024\Data Vizualisation\Project\PrixCarburants_annuel_2022.xml")
root = tree.getroot()

# Process XML data into a list of dictionaries
data_list = [process_xml_element(x) for x in root]

# Create a DataFrame
df = pd.DataFrame(data_list)

# Rename columns and perform data transformations
df = df.rename(columns={"id": "id_gaz", "valeur": "prix", "nom": "gaz", "cp": "code_postal", "maj": "date_releve"})
df["date_releve"] = df["date_releve"].str.replace("T..:..:..", "")
df["date_releve"] = pd.to_datetime(df["date_releve"], format="%Y-%m-%d")
df["prix"] = df["prix"].astype(float) / 1000
df["id"] = df["id2"].apply(lambda x: "0" + str(x) if len(str(x)) == 7 else str(x))
df = df.groupby(["id", "date_releve", "id_gaz"])["prix"].mean().reset_index()
df = df.drop_duplicates().sort_values(by=["id", "id_gaz", "date_releve"])

# Print the resulting DataFrame
print(df)