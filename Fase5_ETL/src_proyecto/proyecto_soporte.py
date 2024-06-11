
#%%
import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import re
from word2number import w2n
import mysql.connector

def initial_exploration(url):
    '''Exploracion inicial de los datos. 
        args-(url) Enlace para la extracción del archivo csv con los datos a examinar.
        return - (serie)informacion básica de las columnas y tipos de valor
                - (serie)Cuerpo de la tabla de datos.
                - (df)Valores estadísticos básicos columnas numéricas.
                - (df)Valores estadísticos básicos columnas categóricas.
                - (serie)Valores nulos
    '''
    try:
        df = pd.read_csv(url, index_col=0)
        print(f"--------------------------------\n")
        print("-------------------------------General file exploration--------------------------------\n")
    except:
        print(f"Error reading file")
    # Entendemos los datos de nuestro DataFrame
    print("--------------------General information------------------------\n")
    print(df.info())
    print("\n------------------------Shape----------------------------------\n")
    print(f"The Dataframe contains {df.shape[0]} rows and {df.shape[1]} columns")
    print("\n------------------------Columns-----------------------------------\n")
    display(pd.DataFrame(df.columns, columns=["columns"]))
    try:
        print("\n------------------------------------Statistics for numeric columns:----------------------------\n")
        display(pd.DataFrame(df.describe().T))
    except:
        print(f"The DataFrame does not contain numeric columns:")
        print("\n--------------------------------------------------------------------\n")
    try:
        print("\n------------------Statistics for categorical columns:-----------------\n")
        display(pd.DataFrame(df.describe(include="O").T)) # incluimos entre los paréntesis el parámetro include = "object"
    except: 
        print(f"The DataFrame does not contain categorical columns")
        print("\n--------------------------------------------------------------------\n")
    print("\n----------------------Data type:-------------------------------\n")
    display(pd.DataFrame(df.dtypes,columns = ["data_type"]))
    print("\n-----------------------Null values:---------------------------\n")
    print(df.isnull().sum()) 
    print("\n----------------------Duplicate rows:--------------------------\n")
    print(df.duplicated().sum())
    print("\n-----------------------------------------------------------------\n")




def import_csv(url):
    ''' importa csv desde la carpeta de trabajoy lo guarda en un dataframe.
    args- 
    url/xpath donde se encuentra el archivo
    return- 
    (df)-data_frame sin la columna 'Unnamed'
    '''
    df_raw=pd.read_csv(url) #importamos csv
    return df_raw.iloc[:, 1:] #seleccionamos solo las columnas que nos interesan.


def check_columns (df, new_columns):
    ''' Checkea las columnas que se introducen manualmente para comprobar que están todas y cambia los nombres en el df antiguo.
        args:   (df) Df del cual se desea hacer los calculos.
                (list) Lista de columnas nuevas.
        return:  (df) Df con los nombres de las columnas actualizados.
    '''
    #Hacemos un if para asegurarnos que no se queda ninguna columna sin nombre
    if len(new_columns)==len(df.columns):
        df.columns=new_columns
        return df
    else:
        raise ValueError('La lista new_columns debe tener la misma longitud que número de columnas tiene el DataFrame.')


#Introducimos las columnas en en el df.
def rename_columns(df, new_col):
    ''' Limpiamos lista de columnas.Renombramos las columnas por valores predefinidos
    args:   (df) Df a modificar
            (list) Lista con una string donde se encuentran los nuevos nombres columnas
    return:  (df) Df con las columnas modificadas.
    '''
    old_columns=df.columns
    lista_new_col1=re.sub("'","", new_col[0])
    lista_new_col=re.split(',', lista_new_col1)
    lista_new=[]
    for i in lista_new_col:
        lista_new.append(i.strip())
    d=dict(zip(old_columns, lista_new))
    df.rename(columns=d, inplace=True)
    return df


def capitalize(df):
    ''' Pasa la primera letra de los titulos de las columnas a mayúscula
    args:   (df) Df a modificar
    return:  (df) Df con las columnas modificadas.
    '''
    df.columns=df.columns.str.capitalize()
    return df


def age_to_int(num):
    ''' modifica aquellos valores que expresan numeros en una string y los pasa a dígitos. Si encuentra valores nulos los pasa a formato np.nan
    args:   (str) str a modificar
    return:  (int64) dígito.
    '''
    try:
        return int(num) #Devuelve el digito en formato intenger.
    except ValueError:
        try:
            return w2n.word_to_num(num) #usamos la función word_to_num() de la libreria word2number
        except ValueError:
            return np.nan # Transformamos los nulos en un formato válido.


def remove_negative_values(df,columna):
    '''Transforma los valores negativos en positivos
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.
    return:  (df) Df con las columnas modificadas.
    '''
    df.loc[df[columna]<0, columna]*=-1
    return df


def extrapolate(valor):
    '''Categoriza los valores en funcion de su valor en cuatro tipos.
    args:   (int) valor a categorizar       
    return:  (int)categoría a la que corresponde en función de su valor.
    '''
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
    

def remove_dollar(df, columns):
    '''Remueve el simbolo $ de una string
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.       
    return:  (df) Df con las columnas modificadas.
    '''
    for i in columns:
        df[i]=df[i].str.replace('$', '', regex=False)
    return df

def change_to_null (string):
    '''Cambia los valores 'Not Available' por valores nulos en un formato válido.
    args:   (str) valor a modificar      
    return:  (str) Valor nulo en formato válido.
    '''
    if string == 'Not Available':
        return np.nan
    else:
        return string

def strip_strings(cell):
    '''Elimina los espacios al principio y final de una string.
    args:   (str) valor a modificar      
    return:  (str) string sin espacios.
    '''
    if isinstance(cell, str): #si es un string retorna sin espacios
        return cell.strip()
    return cell


def male_female(df, column):
    '''transforma los 0 en 'Male' y los 1 en 'Female'
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.       
    return:  (df) Df con las columnas modificadas.
    '''
    df[column]=df[column].replace({0:'Male', 1:'Female'})
    return df


def unify_yes_no(df, columns):
    '''unifica los valores y los clasifica en Yes/No'
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.       
    return:  (df) Df con los valores modificados.
    '''

    yes_no_map={'yes':'Yes', 'YES':'Yes', 'TRUE':'Yes', 'true':'Yes', '1':'Yes', 'Y':'Yes', 'Yes':'Yes',
        'no':'No', 'No':'No', 'NO':'No', 'FALSE':'No', 'false':'No', '0':'No', 'False':'No'}
    
    for i in columns:
        df[i]=df[i].astype(str).map(yes_no_map)
    return df


def int_to_float(df, columns):
    '''Transforma el tipo de valor intenger a float de columnas específicas'
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.       
    return:  (df) Df con los valores modificados.
    '''
    for i in columns:
        df[i]=df[i].astype(float).round(2)
    return df

def object_to_float(df, columns):
    '''Transforma el tipo de valor object a float de columnas específicas. Cambia las ',' por '.''
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.       
    return:  (df) Df con los valores modificados.
    '''
    for i in columns:
        try:
            df[i]=df[i].str.replace(',', '.').astype(float).round(2)
        except:
            df[i]=df[i].astype(float).round(2)
    return df


def capitalize_string(df, columns):
    ''' Pasa la primera letra de los titulos de las columnas a mayúscula de columnas específicas.
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.
    return:  (df) Df con las columnas modificadas.
    '''                                       #! REPETIDO ESTE CODIGO EN LA LIMPIEZA NOMBRES COLUMNA
    for i in columns:
        df[i]=df[i].str.capitalize()
    return df


#Gestión de nulos y eliminación de columnas prescindibles
def null_percentage(df):
    ''' Calcula el porcentaje de valores nulos en las columnas del dataframe.
    args:   (df) Df a modificar
            
    return: (df) Porcenajes de valores nulos por columnas categóricas.
            (list) Porcenajes de valores nulos por columnas numéricas.
    ''' 
    #Separamos las columnas por categóricas y numéricas
    cat_cols=df.select_dtypes(include=['O'])
    num_cols=df.select_dtypes(include=['number'])

    #Calculamos la cantidad y % de nulos de las columnas categóricas
    cat_nulos_df=pd.DataFrame({'Column': cat_cols.columns, #trae los nombres de las columnas
                                'Nulos': cat_cols.isnull().sum(), #trae la suma de los nulos
                                '% Nulos': (cat_cols.isnull().mean() * 100).round(2)}) #trae el % de nulos
    cat_nulos_df=cat_nulos_df[cat_nulos_df['Nulos'] > 0] #filtra para aquellos >0

    #Calculamos la cantidad y % de nulos de las columnas numéricas
    num_nulos_df=pd.DataFrame({'Column': num_cols.columns, #trae los nombres de las columnas
                                'Nulos': num_cols.isnull().sum(), #trae la suma de los nulos
                                '% Nulos': (num_cols.isnull().mean() * 100).round(2)}) #trae el % de nulos

    #Creamos variables en las que guardamos las medias y medianas de cada columna numérica
    num_mean=num_cols.mean()
    num_median=num_cols.median()
    #Añadimos las medias y medianas al df de columnas numéricas
    num_nulos_df['Mean']=num_nulos_df['Column'].map(num_mean)
    num_nulos_df['Median']=num_nulos_df['Column'].map(num_median)

    num_nulos_df=num_nulos_df[num_nulos_df['Nulos'] > 0] #filtra para aquellos >0
    return cat_nulos_df, num_nulos_df


def unknown_data (df): 
    ''' Transforma los valores nulos en el string 'Unknow'
    args:   (df) Df a modificar
            
    return: (df) Df con los valores modificados
    '''
    cat_cols=df.select_dtypes(include=['O'])
    for i in cat_cols:
        df[i]=df[i].fillna('Unknown')
    return df


def media_nulos(df, columns):
    ''' Sustituye los valores nulos de columnas específicas por el promedio del los datos de la misma.
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.
    return:  (df) Df con las columnas modificadas.
    ''' 
    for i in columns:
        imputer=SimpleImputer(strategy='mean')
        df[i]=imputer.fit_transform(df[[i]])
        df[i]=round(df[i], 2)
    return df


def iterative_nulos(df, columns):
    ''' Sustituye los valores nulos de columnas específicas por un valor estimado mediante el método estadístico Interative Imputer
    args:   (df) Df a modificar
            (list) Lista de columnas a modificar.
    return:  (df) Df con las columnas modificadas.
    ''' 
    for i in columns:
        imputer=IterativeImputer(max_iter=20, random_state=42)
        df[i]=imputer.fit_transform(df[[i]])
        df[i]=round(df[i], 2)
    return df

# %%
