# Query creación BBDD

query_create_bbdd = "CREATE DATABASE IF NOT EXISTS peoplemetrics"

# Query cración de las tablas

query_table_employees="CREATE TABLE IF NOT EXISTS Employees(Id_employees INT AUTO_INCREMENT PRIMARY KEY,employee_count FLOAT,Gender ENUM('Male', 'Female') NOT NULL,Age INT, Marital_status VARCHAR(25), Over_18 VARCHAR (25), Date_birth INT, Employee_number VARCHAR (25));"
query_table_job_details="CREATE TABLE IF NOT EXISTS Job_details(Id_employees INT AUTO_INCREMENT PRIMARY KEY,Job_role VARCHAR(100), Job_level INT,Business_travel VARCHAR(100), Job_involvement INT, Over_time ENUM('Yes', 'No','Unknown') NOT NULL, Remote_work ENUM('Yes', 'No','Unknown') NOT NULL, Years_at_company INT, Years_since_last_promotion INT, Years_with_curr_manager INT);"
query_table_employee_profile="CREATE TABLE IF NOT EXISTS Employee_profile (Id_employees INT AUTO_INCREMENT PRIMARY KEY,Education INT,Education_field VARCHAR(100),Num_companies_worked INT,Total_working_years FLOAT);"
query_table_salary="CREATE TABLE IF NOT EXISTS Salary (Id_employees INT AUTO_INCREMENT PRIMARY KEY,Hourly_rate FLOAT, Daily_rate FLOAT, Monthly_rate FLOAT, Percent_salary_hike FLOAT, Stock_option_level INT,Training_times_last_year INT);"
query_table_employee_company="CREATE TABLE IF NOT EXISTS Employee_company(Id_employees INT AUTO_INCREMENT PRIMARY KEY,Attrition ENUM('Yes', 'No') NOT NULL,Environment_satisfaction INT,Job_satisfaction INT,Performance_rating FLOAT,Relationship_satisfaction INT,Work_life_balance FLOAT,Distance_from_home FLOAT);"

# Query inserción datos en tablas

query_insert_data_employees="INSERT INTO Employees (Employee_count, Gender, Age, Marital_status, Over_18, Date_birth, Employee_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"
query_insert_data_employee_profile="INSERT INTO Employee_profile (Education, Education_field, Num_companies_worked, Total_working_years) VALUES (%s, %s, %s, %s)"
query_insert_data_job_details="INSERT INTO Job_details (Job_role,Job_level,Business_travel,Job_involvement,Over_time,Remote_work,Years_at_company,Years_since_last_promotion,Years_with_curr_manager) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query_insert_data_salary="INSERT INTO Salary (Hourly_rate,Daily_rate,Monthly_rate,Percent_salary_hike,Stock_option_level,Training_times_last_year) VALUES (%s,%s,%s,%s,%s,%s)"
query_insert_data_employee_company="INSERT INTO Employee_company(Attrition,Environment_satisfaction,Job_satisfaction,Performance_rating,Relationship_satisfaction,Work_life_balance,Distance_from_home) VALUES (%s,%s,%s,%s,%s,%s,%s)"