import pandas as pd
import os
import numpy as np
from io import StringIO
buffer=StringIO()
import re
pd.set_option('display.max_columns', None)

def generate_report(nombre_fichero):
    #Importamos csv
    #url=('https://raw.githubusercontent.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/main/HR%20RAW%20DATA.csv')
    
    if ".csv" in nombre_fichero: 
        try:  
            df=pd.read_csv(nombre_fichero)
        except:
            print("Error while reading the file")
            exit()
    elif ".xlsx" in nombre_fichero:
        df=pd.read_excel(nombre_fichero)
    else:
        print("No valid extension")
        exit()

    #Entendemos la estuctura de los datos:

    head=df.head() #Mostramos las primeras filas del DataFrame
    tail=df.tail() #Mostramos las últimas filas del DataFrame
    info=df.info(buf=buffer) #Visualizamos la información básica del DataFrame
    info_str=buffer.getvalue()
    #Visualizamos cuántas filas y columnas tenemos
    shape_row=df.shape[0]
    shape_columns=df.shape[1]

    #print(f'El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas')

    colums_name=df.columns #Mostramos los nombres de las columnas

    #Visualizamos en qué columnas hay nulos y cuántos hay
    null=df.isnull().sum()[df.isnull().sum()>0]

    #Visualizamos si existe algún valor duplicado
    duplicated_row=df.duplicated().sum()
    try:
        f = open("dataframe_report.txt", "x")
    except:
        f = open("dataframe_report.txt", "w")
    f.write(f"This is the report of the file:{nombre_fichero}\n")
    f.write("\n-----------------------------------------------\n")
    f.write("------------------INFO---------------------------\n")
    f.write("-------------------------------------------------\n")
    f.write(info_str)
    f.write("\n-----------------------------------------------\n")
    f.write("------------------SHAPE--------------------------\n")
    f.write("-------------------------------------------------\n")
    f.write(str(f'The DataFrame has {df.shape[0]} rows and {df.shape[1]} columns'))
    f.write("\n-----------------------------------------------\n")
    f.write("------------------COLUMNS_NAME-------------------\n")
    f.write("-------------------------------------------------\n")
    f.write(str(colums_name))
    f.write("\n-----------------------------------------------\n")
    f.write("------------------NULL_VALUES--------------------\n")
    f.write("-------------------------------------------------\n")
    f.write(str(null))
    f.write("\n-----------------------------------------------\n")
    f.write("------------------DUPLICATED_ROW-----------------\n")
    f.write("-------------------------------------------------\n")
    f.write(str(duplicated_row))
    f.close()

nombre_fichero=input("Please, provide file name including extension(csv, xlsx): ")

generate_report(nombre_fichero)