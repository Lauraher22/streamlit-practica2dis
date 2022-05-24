
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#READ EXCEL
#@st.cache
st.set_page_config(layout = "wide")

df = pd.read_csv('https://raw.githubusercontent.com/Lauraher22/streamlit-practica2dis/main/penguins_clear.csv',sep=',',decimal='.')


#SIDEBAR
st.sidebar.header("Selección de filtros:")
species = st.sidebar.multiselect(
    "Selecciona el tipo de pingüino:",
    options=df["species"].unique(),
    default=df["species"].unique()
)

island = st.sidebar.multiselect(
    "Selecciona la isla:",
    options=df["island"].unique(),
    default=df["island"].unique(),
)

sex = st.sidebar.multiselect(
    "Selecciona el sexo",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

df_selection = df.query(
    "species == @species & island ==@island & sex == @sex"
)

#MAINPAGE

st.markdown("DISEÑO Y PROGRAMACIÓN DE HERRAMIENTAS ANALÍTICAS")
st.markdown("ACTIVIDAD 2: DESARROLLO DE HERRAMIENTA ANALÍTICA")
st.markdown("Laura Hernández Pita")
st.title("Conjunto de datos de pingüinos del archipiélago Palmer (Antártida)")
st.markdown("##")

#KPI's
st.subheader("Medias de los datos: ")
culmen_length_mean = round(df_selection["culmen_length_mm"].mean(), 1)
culmen_depth_mean = round(df_selection["culmen_depth_mm"].mean(), 1)
flipper_length_mean = round(df_selection["flipper_length_mm"].mean(), 1)
body_mass_mean = round(df_selection["body_mass_g"].mean(), 1)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.text("Longitud del culmen (mm):")
    st.subheader(f"{culmen_length_mean}")
    st.text("Profundidad del culmen(mm):")
    st.subheader(f"{culmen_depth_mean}")
with middle_column:

    st.text("Altura (mm):")
    st.subheader(f"{flipper_length_mean}")
with right_column:
    st.text("Peso (g):")
    st.subheader(f"{body_mass_mean}")


st.subheader("Graficos de los datos: ")

page = st.sidebar.selectbox('Seleccione el tipo de gráfico',['Histograma','BoxPlot', 'Circular'])





if page =='Histograma':
    
    hist_body_mass = px.histogram(df_selection,x="body_mass_g", color="species",title=("Peso del pingüino:"), color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(hist_body_mass)

    hist_culmen_length = px.histogram(df_selection,x="culmen_length_mm",color="species",title=("Longitud del culmen:"), color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(hist_culmen_length)

    hist_culmen_depth = px.histogram(df_selection,x="culmen_depth_mm",color="species",title=("Profundidad del culmen:"),color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(hist_culmen_depth)
    
    hist_flipper_length = px.histogram(df_selection,x="flipper_length_mm",color="species",title=("Altura del pingüino:"),color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(hist_flipper_length)
    
elif page =='Circular':
    
    pie_species = px.pie(df_selection,names="species",title=("% cantidad por especies"),color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(pie_species)
    pie_island = px.pie(df_selection,names="island",title=("% cantidad por isla"), color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(pie_island)
    pie_sexo = px.pie(df_selection,names="sex",title=("% cantidad por sexo"),color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(pie_sexo)

    
else:

    box_body_mass = px.box(df_selection,x="body_mass_g", color="species",title=("Peso del pingüino:"), color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(box_body_mass)

    box_culmen_length = px.box(df_selection,x="culmen_length_mm", color="species",title=("Longitud del culmen:"), color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(box_culmen_length)

    box_culmen_depth = px.box(df_selection,x="culmen_depth_mm", color="species",title=("Profundidad del culmen:"),color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(box_culmen_depth)
    
    box_flipper_length = px.box(df_selection,x="flipper_length_mm", color="species",title=("Altura del pingüino:"),color_discrete_sequence=px.colors.sequential.RdBu)
    st.write(box_flipper_length)
    



