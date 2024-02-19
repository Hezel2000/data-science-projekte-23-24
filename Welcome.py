import streamlit as st
import pandas as pd
from streamlit_player import st_player

st.title('Data Science 23-24 Projekte')

video_list = pd.read_csv('data/data-science-videos-23-24.csv')

tab1, tab2 = st.tabs(['Projekte', 'Bewertung'])

with tab1:
    sel_project = st.selectbox('Wähle ein Projekt', video_list['Titel'])
    fil = video_list['Titel'] == sel_project
    vim_link = video_list[fil]['Vimeo_Link'].tolist()[0]

    col1, col2 = st.columns([70,30])
    with col1:
        st_player(vim_link)
    with col2:
        with st.expander('Dauer', expanded=True):
            st.write(video_list[fil]['Dauer'].tolist()[0])
        with st.expander('Zusatz-Material', expanded=True):
            if video_list[fil]['supplement'].tolist()[0] != 'none available':
                st.write("[Download](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/Basics_Function_plotting_with_the_numpy_package.ipynb" + ")")
            else:
                'keines vorhanden'

with tab2:
    st.subheader('Fragen zur Projekt-Bewertung')
    st.write('*Nur Personen die ein Video abgegeben haben dürfen bewerten, und nur einmal!**')
    
    st.write('Die Bewertungen der beiden Betreuer sind die allein für die Note zählenden, und werden ohne Blick auf die von Euch abgegeben Bewertungen gemacht. Eure Bewertungen dienen zum Vergleich bei der Abschlussbesprechung.')
    st.write('Bewertungen können – müssen nicht – bis zum So, 3. März 2024 23:59 Uhr abgegeben werden.')
    st.link_button('Zur Bewertungsseite', 'https://docs.google.com/forms/d/1KJ_Lwj4UzaVB_vdra4z9yaY2yM_uB5ZxxPW1zVJ7pLk/edit')

    # st.divider()
    # st.write("1. Es wird verständlich in die Aufgabenstellung eingeführt")
    # st.write("2. Die Fragestellung ist klar")
    # st.write("3. Das Video ist gut und nachvollziehbar strukturiert")
    # st.write("4. Die Fragestellung wird im Programm gut umgesetzt")
    # st.write("5. Das Programm ist umfangreich und vielseitig")
    # st.write("6. Das Video ist geeignet, den Sachverhalt der Aufgabenstellung zu erlernen")
    # st.write("7. Der Inhalt hat ein anspruchsvolles Niveau")
    # st.write("8. Die Länge des Videos war der Aufgabenstellung angemessen")
    # st.write("9. Es wurde verständlich gesprochen")
    # st.write("10. Der Sprechgeschwindigkeit konnte man gut folgen")
    # st.write("Folgendes hat mir gut gefallen")
    # st.write("Folgendes hat mir NICHT gut gefallen")
    # st.write("Folgendes könnte verbessert werden")
    # st.write("Gesamt-Bewertung")

#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('data/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")