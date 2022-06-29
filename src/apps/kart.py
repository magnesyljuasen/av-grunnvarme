import streamlit as st
import requests 
import pydeck as pdk
import pandas as pd
from PIL import Image

from src.diverse.funksjoner import Location

def kart_app():
    st.title("Kart")

    
    st.header("Generelt kart")
    st.write("""Kartet gir en rask oversikt over grunnforhold, og andre relevante datasett. 
    Trykk på lag-ikonet i venstre hjørne for å skru av og på lag.""")
    image = Image.open('src/bilder/generelt_kart.png')
    st.image(image)  
    #st.markdown(""" <iframe width="100%" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://asplanviak.maps.arcgis.com/apps/instant/basic/index.html?appid=901e9d0f94b24ec186bd4e1f7ce426c6"></iframe> """, unsafe_allow_html=True)
    url = "https://asplanviak.maps.arcgis.com/apps/instant/basic/index.html?appid=901e9d0f94b24ec186bd4e1f7ce426c6"
    st.header("[Gå til generelt kart](%s)" % url)
    st.markdown("---")
    st.header("Test av NGU sine APIer")
    with st.expander("API - test"):    
        
        location = Location() 
        lat, long = location.address_to_coordinate(location.input())
        
        lat = st.number_input('Breddegrad', value=lat, step=0.0001)
        long = st.number_input('Lengdegrad', value=long, step=0.0001)
        
        

        df = pd.DataFrame({'latitude': [lat],'longitude': [long]})

        init = pdk.Layer(
                    type='ScatterplotLayer',
                    data=df,
                    get_position='[longitude, latitude]',
                    pickable=True,
                    stroked=True,
                    radius_max_pixels=10,
                    radius_min_pixels=500,
                    filled=True,
                    line_width_scale=25,
                    line_width_max_pixels=5,
                    get_fill_color=[255, 195, 88],
                    get_line_color=[0, 0, 0])

        diff = 0.02

        x1 = long - diff
        x2 = lat - diff
        x3 = long + diff
        x4 = lat + diff

        antall = 100
        
        endpoint = f'https://ogcapitest.ngu.no/rest/services/granada/v1/collections/broennparkbroenn/items?f=json&limit={antall}&bbox={x1}%2C{x2}%2C{x3}%2C{x4}'
        r = requests.get(endpoint)
        data = r.json()
        
        st.write(data)

        geojson = pdk.Layer(
        "GeoJsonLayer",
        data,
        pickable=True,
        stroked=True,
        filled=False,
        line_width_scale=50,
        line_width_max_pixels=100,
        get_line_color=[0, 0, 255],
        extruded=True,
        wireframe=True,
        get_elevation='properties.boret_lengde_til_berg * 200')

        st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/streets-v11',
                initial_view_state=pdk.ViewState(
                latitude=lat,
                longitude=long,
                pitch=45,
                bearing=0
                ),
                layers=[geojson, init]))
    
    

    

    
    

