#%%
import os
from dotenv import load_dotenv
from src_proyecto import proyecto_soporte as ps
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
df_data=ps.import_csv(url1)
#Visualizamos el número total de filas y de columnas
print(f'Cantidad de filas: {df_data.shape[0]}\nCantidad de columnas: {df_data.shape[1]}')


#%%
#limpiamos las columnas.
#Al haberlas arreglado parcialmente a mano, importamos la lista con las nuevas columnas.
data = open("columns_handmade.txt", "r")#Esta funcion no es parte del soporte por lo que no ha<cer falta que lleve.api
new_columns = list(data)
print(new_columns)

#%%
#Introducimos las columnas en en el df.
def rename_columns(df, new_col):
    ''' Limpiamos lista de columnas.Renombramos las columnas por valores predefinidos
    args:   (df) Df a modificar
            (list) Lista con una string donde se encuentran los nuevos nombres columnas
    return:  (df) Df con las columnas modificadas.'''
    old_columns=df.columns
    lista_new_col1=re.sub("'","", new_col[0])
    lista_new_col=re.split(',', lista_new_col1)
    lista_new=[]
    for i in lista_new_col:
        lista_new.append(i.strip())
    print(lista_new)
    d=zip(old_columns, lista_new)
    df.rename(columns=d, inplace=True)
    return df
#%%
rename_columns(df_data,new_columns)
df_data.head(1)



#%%
#nos aseguramos que la lista tiene el numero de columnas correctas:
df_data=ps.check_columns(new_columns)
# %%
def capitalize(df):
    df.columns=df.columns.str.capitalize()
    return df

# %%
