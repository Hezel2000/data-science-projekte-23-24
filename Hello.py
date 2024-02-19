import streamlit as st
import pandas as pd
from streamlit_player import st_player

st.title('Data Science 23-24 Projekte')

vimeo_list = pd.read_csv('data/data-science-videos-23-24.csv')

st.write(vimeo_list)



#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('data/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")