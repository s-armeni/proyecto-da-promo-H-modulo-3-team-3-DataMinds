
# %%
import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import re
# %%
def import_csv(url):
    ''' importa csv desde la carpeta de trabajoy lo guarda en un dataframe.
    args- 
    url/xpath donde se encuentra el archivo
    return- 
    (df)-data_frame sin la columna 'Unnamed'
    '''
    df_raw=pd.read_csv(url) #importamos csv
    return df_raw.iloc[:, 1:] #seleccionamos solo las columnas que nos interesan.
# %%
def cleck_columns (df, new_columns):
    #Hacemos un if para asegurarnos que no se queda ninguna columna sin nombre
    if len(new_columns)==len(df.columns):
        df.columns=new_columns
        return df
    else:
        raise ValueError('La lista new_columns debe tener la misma longitud que número de columnas tiene el DataFrame.')

#%%
def capitalize(df):
    df.columns=df.columns.str.capitalize()
    return df
# %%
def age_to_int(num):
    try:
        return int(num)
    except ValueError:
        try:
            return w2n.word_to_num(num)
        except ValueError:
            return np.nan

# %%
def remove_caracter(df,columna):
    df.loc[df[columna]<0, columna]*=-1
    return df
# %%
def extrapolate(valor):
    if 4>=valor:
        return valor
    elif 4<valor<=10:
        return 1
    elif 10<valor<=20:
        return 1
    elif 20<valor<=30:
        return 2
    elif 30<valor<=40:
        return 3
    elif valor>40:
        return 4
# %%
def remove_dollar(df, columns):
    for i in columns:
        df[i]=df[i].str.replace('$', '', regex=False)
    return df
# %%
def change_to_null (string):
    if string == 'Not Available':
        return np.nan
    else:
        return string
# %%
def strip_strings(cell):
    if isinstance(cell, str): #si es un string retorna sin espacios
        return cell.strip()
    return cell
# %%
def male_female(df, column):
    df[column]=df[column].replace({0:'Male', 1:'Female'})
    return df
# %%
def unify_yes_no(df, columns):
    yes_no_map={'yes':'Yes', 'YES':'Yes', 'TRUE':'Yes', 'true':'Yes', '1':'Yes', 'Y':'Yes', 'Yes':'Yes',
        'no':'No', 'No':'No', 'NO':'No', 'FALSE':'No', 'false':'No', '0':'No', 'False':'No'}
    
    for i in columns:
        df[i]=df[i].astype(str).map(yes_no_map)
    return df
# %%
def int_to_float(df, columns):
    for i in columns:
        df[i]=df[i].astype(float).round(2)
    return df
# %%
def object_to_float(df, columns):
    for i in columns:
        try:
            df[i]=df[i].str.replace(',', '.').astype(float).round(2)
        except:
            df[i]=df[i].astype(float).round(2)
    return df
# %%
def capitalize_string(df, columns): #! REPETIDO ESTE CODIGO EN LA LIMPIEZA NOMBRES COLUMNA
    for i in columns:
        df[i]=df[i].str.capitalize()
    return df
# %%
