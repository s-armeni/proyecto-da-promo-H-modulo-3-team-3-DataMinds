# importamos las librerías que necesitamos
# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd

# Manejo de cadenas
# -----------------------------------------------------------------------
from io import StringIO
buffer=StringIO() #objeto de StringIO que actúa como buffer en memoria para cadenas de texto

# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

def generate_report(nombre_fichero):
    """
    Esta función genera un informe detallado de un archivo CSV o Excel
    incluyendo información básica sobre la estructura del DataFrame, nombre de
    columnas, valores nulos y filas dusplicadas.
    
    Parámetro:
    nombre_fichero: El nombre del archivo a leer (debe incluir la extensión '.csv' o '.xlsx'), obtenido mediante un input.
    
    """
    if ".csv" in nombre_fichero:
        try:  
            df=pd.read_csv(nombre_fichero) #Lee el archivo en un DataFrame de pandas
        except:
            print("Error while reading the file")
            exit() #SystemExit: si el archivo no se puede leer
    elif ".xlsx" in nombre_fichero:
        df=pd.read_excel(nombre_fichero)
    else:
        print("No valid extension")
        exit() #SystemExit: si la extensión del archivo no es '.csv' o '.xlsx'


    head=df.head() #Mostramos las primeras filas del DataFrame
    tail=df.tail() #Mostramos las últimas filas del DataFrame
    
    #Visualizamos la información básica sobre el DataFrame
    info=df.info(buf=buffer) # genera info sobre el DataFrame y la almacena en el buffer 
    info_str=buffer.getvalue() # se extraen los datos del buffer como una cadena para después escribirlos en un archivo de texto    
    
    #Visualizamos la forma del DataFrame
    shape_row=df.shape[0] # número de filas
    shape_columns=df.shape[1] # número de columnas

    colums_name=df.columns #Mostramos los nombres de las columnas

    #Visualizamos en qué columnas hay nulos y cuántos hay
    null=df.isnull().sum()[df.isnull().sum()>0]

    #Visualizamos las filas duplicadas
    duplicated_row=df.duplicated().sum()


    try:
        f = open("dataframe_report.txt", "x")
    except:
        f = open("dataframe_report.txt", "w")
    f.write(f"This is the report of the file: {nombre_fichero.upper()}\n")
    f.write("\n-------------------------------------------------\n")
    f.write("--------------------INFO-------------------------\n")
    f.write("-------------------------------------------------\n")
    f.write(info_str)
    f.write("\n---------------------------------------------------\n")
    f.write("--------------------SHAPE--------------------------\n")
    f.write("---------------------------------------------------\n")
    f.write(str(f'The DataFrame contains {df.shape[0]} rows and {df.shape[1]} columns'))
    f.write("\n---------------------------------------------------\n")
    f.write("------------------COLUMNS_NAME---------------------\n")
    f.write("---------------------------------------------------\n")
    f.write(str(colums_name))
    f.write("\n---------------------------------------------------\n")
    f.write("------------------NULL_VALUES----------------------\n")
    f.write("---------------------------------------------------\n")
    f.write(str(null))
    f.write("\n---------------------------------------------------\n")
    f.write("------------------DUPLICATED_ROW-------------------\n")
    f.write("---------------------------------------------------\n")
    f.write(str(duplicated_row))
    f.close()

nombre_fichero=input("Please, provide file name including extension(csv, xlsx): ")

generate_report(nombre_fichero)