import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

def pca_maker(data_import):
    #we separate categorical columns and numerical columns
    numerical_columns_list = []
    categorical_columns_list = []

    #function to separate categorical columns and numerical columns
    for i in data_import.columns:
        if data_import[i].dtype == np.dtype("float64") or data_import[i].dtype == np.dtype("int64"):
            numerical_columns_list.append(data_import[i])
        else:
            categorical_columns_list.append(data_import[i])

    #create a dataframe of numerical column created
    numerical_data=pd.concat(numerical_columns_list,axis=1)
    #create a dataframe of categorical column created
    categorical_data=pd.concat(categorical_columns_list,axis=1)

    #replacing the null values with mean values in numerical_data
    numerical_data=numerical_data.apply(lambda x: x.fillna(np.mean(x)))

    #pandas dataframe got scaled into 2d numpy array
    scaler = StandardScaler()

    #fit_transform is done together.
    scaled_values = scaler.fit_transform(numerical_data)

    #create pca object
    pca = PCA()

    pca_data = pca.fit_transform(scaled_values)
    #attaching back to the dataframe
    pca_data = pd.DataFrame(pca_data)
    pca_data

    #first we create dictionary of original column names
    #using list comprehension(way to create list from a for loop in one line)
    new_column_names = ["PCA_" + str(i) for i in range(1, len(pca_data.columns) + 1)]

    list(pca_data.columns)
    #now we have two lists and we need to convert them into key/value pairs
    column_mapper = dict(zip(list(pca_data.columns),new_column_names))

    #changing column names for our convience
    pca_data = pca_data.rename(columns=column_mapper)

    output = pd.concat([data_import,pca_data],axis=1)
    
    return output,list(categorical_data.columns),new_column_names