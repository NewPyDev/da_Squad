import json
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
squad_logo = load_lottiefile('lottiefiles/squad.json')
controller_logo = load_lottiefile('lottiefiles/cotroller.json')
dis_link = 'https://discord.gg/v3FDUQ5t'
logo = Image.open('images/logo.png')
st.set_page_config(page_title="The Squad", page_icon=logo, layout='wide')
#--- sidebar---
st.sidebar.title('The Squad')
with st.sidebar:
    st_lottie(squad_logo,speed=2, loop=True, height=150, width=150)
st.sidebar.header('Members:')
st.sidebar.write('[Nagat__0#](https://steamcommunity.com/id/seike-nagato)')
st.sidebar.write('[Wahio](https://steamcommunity.com/id/wahiokiller/)')
st.sidebar.write('[BloodyShirou](https://steamcommunity.com/profiles/76561198836547637/)')
st.sidebar.write('[Frost](https://steamcommunity.com/id/frostdz13/)')
st.sidebar.write('[Kail0o#](https://steamcommunity.com/profiles/76561197975327133/)')
st.sidebar.write('[Markus](https://steamcommunity.com/profiles/76561199262417175/)')
st.sidebar.write('[Discord](https://discord.gg/PEjvzxtZhb)')
#---main page---
with st.container():
    st.subheader("The Squad is here! 🔥")
    st.title("A gaming team from Algeria")

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('style/style.css')

with st.container():
    st.write("---")
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st_lottie(controller_logo, speed=1, loop=True, height=300, width=300)
    with right_column:
        st.header("What we play")
        st.write("##")
        st.write("Rainbow six seige")
        st.write("Counter-Strike 1.6")
        st.write("Counter-Strike Global offensive")
        st.write("Msaset Riad")








