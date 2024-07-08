import streamlit as st
import mag4 as mg
import plotly.express as px

mg_datasets = mg.available_datasets()
fil = mg_datasets['Source'] == 'Georoc'
georoc_datasets = mg_datasets[fil]['Title']
elements = mg.get_data('emei').columns.tolist()[27:]

def plot_data(x_el, y_el, dataset):
    df = mg.get_data(dataset)
    x_el_data = df[x_el]/10000
    y_el_data = df[y_el]/10000
    fig = px.scatter(df, x=x_el_data, y=y_el_data, title=dataset)
    fig.update_layout(xaxis_title=f'{x_el} (wt%)', yaxis_title=f'{y_el} (wt%)')
    st.plotly_chart(fig)

col1, col2 = st.columns([30, 70])

with col1:
    sel_dataset = st.selectbox('Select Dataset', georoc_datasets)
    sel_x_el = st.selectbox('Select x-axis', elements)
    sel_y_el = st.selectbox('Select y-axis', elements)

with col2:
    plot_data(sel_x_el, sel_y_el, sel_dataset)