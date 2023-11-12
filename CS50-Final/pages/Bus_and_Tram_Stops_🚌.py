import streamlit as st
from streamlit_folium import st_folium
import folium
import requests


st.sidebar.markdown("# Bus and Tram Stops")

st.title("Bus & Tram Stops")
# ------------------ Bus/Tram Stops -----------------
stationsapi = requests.get("https://www.poznan.pl/mim/plan/map_service.html?mtype=pub_transport&co=cluster").json()
stations = stationsapi["features"]

m = folium.Map(location=[52.402774, 16.917845], zoom_start=13)

for station in stations:
    coordinatesFlipped = station["geometry"]["coordinates"]
    coordinates = [coordinatesFlipped[1], coordinatesFlipped[0]]
    properties = station["properties"]
    name = f"{properties['stop_name']}"
    other = f"Zone:{properties['zone']}\nLines:{properties['headsigns']}"
    folium.Marker(
        coordinates,
        popup=f"{name}\n{other}",
        tooltip=name
    ).add_to(m)

st_data = st_folium(m, width=725)