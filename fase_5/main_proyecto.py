#%%
import os
from dotenv import load_dotenv
from src_proyecto import api_proyecto_soporte as api
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import re

# %%
print('===============================================================\n')
print('EDA\n')
print('===============================================================\n')

#%%
#Importamos csv.

url1=('https://raw.githubusercontent.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/main/HR%20RAW%20DATA.csv')#!utilizamos url para que sea reproducible en otros ordenadores

# %%
df_data=api.import_csv(url1)
#Visualizamos el número total de filas y de columnas
print(f'Cantidad de filas: {df_data.shape[0]}\nCantidad de columnas: {df_data.shape[1]}')


#%%
#limpiamos las columnas.
#Al haberlas arreglado parcialmente a mano, importamos la lista con las nuevas columnas.
data = open("columns_handmade.txt", "r")
new_columns = list(data)
print(new_columns)

#%%
#nos aseguramos que la lista tiene el numero de columnas correctas:
df_data=check_columns(new_columns)
# %%
def capitalize(df):
    df.columns=df.columns.str.capitalize()
    return df

# %%
