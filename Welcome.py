import streamlit as st
import pandas as pd
from streamlit_player import st_player

st.title('Data Science 23-24 Projekte')

video_list = pd.read_csv('data/data-science-videos-23-24.csv')

sel_project = st.selectbox('Wähle ein Projekt', video_list['Titel'])
fil = video_list['Titel'] == sel_project
vim_link = video_list[fil]['Vimeo_Link'][0]

col1, col2 = st.columns([70,30])

with col1:
    st_player(vim_link)

with col2:
    with st.expander('Dauer', expanded=True):
        st.write(video_list[fil]['Dauer'][0])
    with st.expander('Zusatz-Material', expanded=True):
        st.link_button('Download', video_list[fil]['supplement'][0])

#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('data/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")