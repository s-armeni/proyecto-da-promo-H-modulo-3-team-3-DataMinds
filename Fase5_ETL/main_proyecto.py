
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
from word2number import w2n
from src_proyecto import soporte_queries_creacion_bbdd as query
from src_proyecto import bbdd_dataminds_soporte as bbdd
import mysql.connector


print('===============================================================\n')
print('                  Initial data exploration\n')
print('===============================================================\n')

url1=('https://raw.githubusercontent.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/main/HR%20RAW%20DATA.csv')
ps.initial_exploration(url1)



print('===============================================================\n')
print('                  Exploratory Data Analysis\n')
print('===============================================================\n')


#Importamos csv.
url1=('https://raw.githubusercontent.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/main/HR%20RAW%20DATA.csv')#!utilizamos url para que sea reproducible en otros ordenadores

df_data=ps.import_csv(url1)
#Visualizamos el número total de filas y de columnas
print(f'Cantidad de filas: {df_data.shape[0]}\nCantidad de columnas: {df_data.shape[1]}')

#limpiamos las columnas.
#Al haberlas arreglado parcialmente a mano, importamos la lista con las nuevas columnas.
data = open("columns_handmade.txt", "r")#Esta funcion no es parte del soporte por lo que no ha<cer falta que lleve.api
new_columns = list(data)

ps.rename_columns(df_data,new_columns)

def capitalize(df):
    df.columns=df.columns.str.capitalize()
    return df
capitalize(df_data)

df_data['Age']=df_data['Age'].apply(ps.age_to_int)#Estandarización columna 'Age' 

df_data.loc[df_data['Distance_from_home']<0, 'Distance_from_home']*=-1#Eliminamos los '-' de 'Distance_from_home'
df_data['Marital_status']=df_data['Marital_status'].replace('Marreid','married')#Corregimos errores ortográficos en la columna 'Marital_status'
df_data['Environment_satisfaction']=df_data['Environment_satisfaction'].apply(ps.extrapolate)#Aplicamos la funcion anterior a la columna 'Environment_satisfaction'

#Función para eliminar los $
list_dollar=['Daily_rate', 'Salary']
df_data=ps.remove_dollar(df_data, list_dollar)

#Para poder operar con la media y transformalos en float, es necesario pasar el 'not available' a valores nulo nan:
df_data['Hourly_rate']=df_data['Hourly_rate'].apply(ps.change_to_null)

#*Agrupamos las columnas por tipo de limpieza/correción que necesitan.
#Lista de columnas integer a object hombre/mujer
list_male_female=['Gender']
#Lista de columnas yes/no
list_yes_no=['Attrition', 'Over_18', 'Over_time', 'Remote_work']
#Lista de columnas integer a float
list_int_float=['Distance_from_home', 'Employee_count', 'Monthly_rate', 'Percent_salary_hike']
#Lista de columnas object a float
list_object_float=['Daily_rate', 'Hourly_rate', 'Monthly_income', 'Standard_hours', 'Same_as_monthly_income', 'Salary']
#Lista de columnas object a integer
list_object_integer=['Employee_number', 'Performance_rating', 'Total_working_years', 'Work_life_balance', 'Years_in_current_role']

# Eliminamos posibles espacios en blanco al principio y final de las celdas.
df_data=df_data.applymap(ps.strip_strings) #.applymap() porque lo aplico a cada elemento del df

#Estandarizamos la columna de género.
df_data=ps.male_female(df_data, 'Gender')

#Estandarizamos las columnas de 'Yes/No'.
df_data=ps.unify_yes_no(df=df_data, columns=list_yes_no)

#Estandarizamos columnas integer a float.
df_data=ps.int_to_float(df_data, list_int_float)

# Estandarizamos columnas object a float.
df_data=ps.object_to_float(df_data, list_object_float)

#Estandarizamos columnas object a integer.
df_data[['Employee_number', 'Performance_rating', 'Total_working_years', 'Work_life_balance', 'Years_in_current_role']] = df_data[['Employee_number', 'Performance_rating', 'Total_working_years', 'Work_life_balance', 'Years_in_current_role']].replace(',0', '', regex=True).astype(float).astype(pd.Int64Dtype()) #esta parte permite convertir a integer y que se mantengan los nulos existentes

#Unificamos todos los textos
cat_cols=df_data.select_dtypes(include=['O'])
df_data=ps.capitalize_string(df_data, cat_cols)


#Gestión de nulos y eliminación de columnas prescindibles
cat_null,num_null=ps.null_percentage(df_data)

'''Observando los nulos y sus %, decidimos eliminar las siguientes columnas:
Department 81.29% nulos.
Role_departament 81.29% nulos.'''
df_data.drop(['Department', 'Role_departament'], axis=1, inplace=True)


'''Observando los altos % de nulos en el resto de columnas categóricas, decidimos sustituir los valores NaN por 'Unknown' para no alterar la veracidad de los datos.'''
ps.unknown_data(df_data)

df_data.drop(['Monthly_income', 'Standard_hours', 'Years_in_current_role', 'Same_as_monthly_income', 'Number_children', 'Salary'], axis=1, inplace=True)

#Columna Employee_number. Para que la empresa pueda seguir utilizando este identificador a nivel interno:
#Convertimos la columna a object
df_data['Employee_number']=df_data['Employee_number'].astype('object')
#Sustituimos los nullos por 'unkown'.
df_data['Employee_number']=df_data['Employee_number'].fillna('Unknown')

#Para las columnas con un % de nulos inferior al 10%:
#Reemplazamos nulos con la media
columns_mean=['Daily_rate', 'Hourly_rate', 'Work_life_balance']
ps.media_nulos(df_data,columns_mean)

#Reemplazamos nulos con IterativeImputer
columns_iterative_imputer=['Performance_rating', 'Total_working_years']
ps.iterative_nulos(df_data,columns_iterative_imputer)

df_data.to_csv('hr_data_final_etl.csv')



print('===============================================================\n')
print('                  Loading Data \n')
print('===============================================================\n')


bbdd.create_bbdd(query.query_create_bbdd, "AlumnaAdalab")

bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_employees)

bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_job_details)

bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_employee_profile)

bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_salary)

bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_employee_company)

bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_employees, bbdd.data_employees)

bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_employee_profile,bbdd.data_employee_profile)

bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_job_details,bbdd.data_job_details)

bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_salary,bbdd.data_salary)

bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_employee_company,bbdd.data_employee_company)
# %%
