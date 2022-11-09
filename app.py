import pandas as pd
import streamlit as st
import plotly.express as px
from app_fn import pca_maker

#to make the webpage border in size
st.set_page_config(layout="wide")

st.header("Dashboard for Mutidimensional anaylsis of any csv file ")
st.text("Upload a csv file containing numerical and categorical value,then change the axis to see different point of view towards data")


#giving size to the columns
scatter_column,settings_column = st.columns((4,1))

#giving title to the column
scatter_column.title("Multidimensional Analysis")

#giving title to the column
settings_column.title("Settings")

#people can upload data
uploaded_file = settings_column.file_uploader("choose File")

#giving condition if file is uploaded or not
if uploaded_file is not None:
    #reading uploaded file
    data_import = pd.read_csv(uploaded_file)
    
    #giving names to the variables present in app_fn
    pca_data,cat_cols,pca_cols = pca_maker(data_import)
    
    
    categorical_variable = settings_column.selectbox("Variable Select",options=cat_cols)
    categorical_variable_2 = settings_column.selectbox("Second Variable Select",options=cat_cols)
    
    #selecting pca 1 and pca 2
    pca_1=settings_column.selectbox("First Principle Component", options=pca_cols,index=0)
    
    pca_2 = settings_column.selectbox("Second Principle Component", options=pca_cols)
    
    #now adding scatter plot to data
    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y=pca_2, color=categorical_variable, template="simple_white", height=800, hover_data = [categorical_variable_2]), use_container_width=True)
    
else:
    #else condition
    scatter_column.header("Please choose a file")
    






