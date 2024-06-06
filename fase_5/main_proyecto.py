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


# %%
#Importamos csv
url1=('https://raw.githubusercontent.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/main/HR%20RAW%20DATA.csv')
def importar_csv(url):
    df_raw=pd.read_csv(url)
    return df_raw

# %%
importar_csv(url1).head(1)
# %%
#Variable con los nombres de columna originales
old_columns=df_data.columns.tolist()

#Creamos variable con las palabras separadas mediante '_'
new_columns=['Age', 'Attrition', 'Business_Travel', 'Daily_Rate', 'Department',
       'Distance_From_Home', 'Education', 'Education_Field', 'employee_count',
       'employee_number', 'Environment_Satisfaction', 'Gender', 'Hourly_Rate',
       'Job_Involvement', 'Job_Level', 'Job_Role', 'Job_Satisfaction',
       'Marital_Status', 'Monthly_Income', 'Monthly_Rate', 'NUM_COMPANIES_WORKED',
       'Over_18', 'Over_Time', 'Percent_Salary_Hike', 'Performance_Rating',
       'Relationship_Satisfaction', 'Standard_Hours', 'Stock_Option_Level',
       'TOTAL_WORKING_YEARS', 'Training_Times_Last_Year', 'WORK_LIFE_BALANCE',
       'Years_At_Company', 'Years_In_Current_Role', 'Years_Since_Last_Promotion',
       'YEARS_WITH_CURR_MANAGER', 'Same_As_Monthly_Income', 'Date_Birth', 'Salary',
       'Role_Departament', 'NUMBER_CHILDREN', 'Remote_Work']
#Hacemos un if para asegurarnos que no se queda ninguna columna sin nombre
if len(new_columns)==len(df_data.columns):
    df_data.columns=new_columns
else:
    raise ValueError('La lista new_columns debe tener la misma longitud que número de columnas tiene el DataFrame.')
# %%
def capitalize(df):
    df.columns=df.columns.str.capitalize()
    return df

# %%
