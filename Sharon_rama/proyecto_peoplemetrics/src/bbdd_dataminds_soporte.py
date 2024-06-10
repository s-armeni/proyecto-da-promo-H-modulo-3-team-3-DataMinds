# Importamos librerias para la conexión con MySQL
# -----------------------------------------------------------------------
# %%
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
# %%

def create_bbdd (query, contraseña):
    """
    Creamos una función que nos permite crear una bbdd en MySQL
    donde especificamos los datos para la conexión al servidor
    (usuario y contraseña)
    """
    cnx = mysql.connector.connect(user='root', password=contraseña,host='127.0.0.1')
    mycursor = cnx.cursor()

    try: 
        mycursor.execute(query) 
        print("DataBase successfully created")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
# %%
def create_table (usuario, contraseña, bbdd, query):
    """
    Esta funcion permite crear una tabla en una BBDD en MySQL

    Args:
    - usuario: usuario para la conexion al servidor
    - contraseña: contraseña para la conexión al servidor
    - bbdd: nombre de la bbdd donde queremos crear la tabla
    - query: Consulta para la creacion de la tabla
    """
    cnx = mysql.connector.connect(user=usuario, password=contraseña,
                                host='127.0.0.1', database= bbdd)

    mycursor = cnx.cursor()
        
    try: 
        mycursor.execute(query)
    
        print("Table created")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)

    cnx.close()
# %%

def insert_data(usuario, contraseña, bbdd, query, lista_tuplas):
    """
    Esta funcion nos permite insertar los datos en una tabla de la bbdd en MySQL
    Entre los argumentos, especificamos: 
    - lista_tuplas: lista que contiene las tuplas con los datos a insertar.
    """
    cnx = mysql.connector.connect(
        user=usuario, 
        password=contraseña, 
        host="127.0.0.1", database=bbdd)

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, "row/s inserted.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()

url = "https://raw.githubusercontent.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/main/hr_data_final.csv"

# Cargamos el csv

df=pd.read_csv(url, index_col=0)

# Generamos listas de tuplas con la informarción a insertar para poder insertar los datos

data_table_employees=list(zip(df["Employee_count"].values, df["Gender"].values, df["Age"].values, df["Marital_status"].values, df["Over_18"].values,df["Date_birth"].values, df["Employee_number"].values))
data_table_employee_profile=list(zip(df["Education"].values, df["Education_field"].values,df["Num_companies_worked"].values,df["Total_working_years"].values))
data_table_job_details=list(zip(df["Job_role"].values, df["Job_level"].values, df["Business_travel"].values, df["Job_involvement"].values, df["Over_time"].values,df["Remote_work"].values, df["Years_at_company"].values,df["Years_since_last_promotion"].values, df["Years_with_curr_manager"]))
data_table_salary=list(zip(df["Hourly_rate"].values, df["Daily_rate"].values, df["Monthly_rate"].values, df["Percent_salary_hike"].values, df["Stock_option_level"].values,df["Training_times_last_year"].values))
data_table_employee_company=list(zip(df["Attrition"].values, df["Environment_satisfaction"].values, df["Job_satisfaction"].values, df["Performance_rating"].values, df["Relationship_satisfaction"].values,df["Work_life_balance"].values,df["Distance_from_home"].values))

# Función para convertir los elementos de una lista de tuplas a int

def convertir_int(lista_tuplas):
    datos_tabla_caract_def = []
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(int(elemento))
            except:
                lista_intermedia.append(elemento)
            
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    
    return datos_tabla_caract_def # Devuelve una lista de las mismas tuplas con los elementos convertidos

# Llamamos a la función y convertimos los elementos
data_employee_profile= convertir_int(data_table_employee_profile)
data_employees=convertir_int(data_table_employees)
data_job_details=convertir_int(data_table_job_details)
data_salary=convertir_int(data_table_salary)

# Funcion para convertir los elementos de tipo numpy.float a float

def convertir_float(lista_tuplas):
    datos_tabla_caract_def = []
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(float(elemento))
            except:
                lista_intermedia.append(elemento)
            
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    
    return datos_tabla_caract_def # Devuelve una lista de las mismas tuplas con los elementos convertidos

# Llamamos a la función y convertimos los elementos
data_employee_company=convertir_float(data_table_employee_company) 

