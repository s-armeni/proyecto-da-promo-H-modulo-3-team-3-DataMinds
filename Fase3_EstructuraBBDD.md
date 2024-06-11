![BBDD](https://github.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/blob/main/Captura.PNG)

### Employees

 Id_employees INT AUTO INCREMENT PRIMARY KEY </br>
 Employee_count FLOAT </br>
 Gender ENUM ('Male', 'Female') NOT NULL</br>
 Age INT </br>
 Marital_status VARCHAR (25) </br>
 Over_18 ENUM VARCHAR (25) </br>
 Date_birth INT </br>
 Employee_number VARCHAR (25)</br>

### Job_details

 Id_employees INT AUTO INCREMENT PRIMARY KEY </br>
 Job_role VARCHAR (100) </br>
 Job_level INT</br>
 Business_travel VARCHAR (100)</br>
 Job_involvment INT</br>
 Over_time ENUM('Yes', 'No','Unknown') NOT NULL </br>
 Remote_work ENUM('Yes', 'No','Unknown') NOT NULL </br>
 Years_at_company INT </br>
 Years_since_last_promotion INT <br>
 Years_with_curr_manager INT </br>

### Employee_profile

 Id_employees INT AUTO INCREMENT PRIMARY KEY</br>
 Education INT </br>
 Education_field VARCHAR (100)</br>
 Num_companies_worked INT </br>
 Total_working_years FLOAT </br>

### Salary

 Id_employees INT AUTO INCREMENT PRIMARY KEY </br>
 Hourly_rate FLOAT </br>
 Daily_rate FLOAT </br>
 Monthly_rate FLOAT </br>
 Percent_salary_hike FLOAT </br>
 Stock_option_level INT </br>
 Training_times_last_year INT </br>

### Employee_company
 
 Id_employee INT AUTO INCREMENT PRIMARY KEY </br>
 Attrition ENUM('Yes', 'No') NOT NULL </br>
 Environment_satisfaction  INT </br>
 Job_satisfaction INT </br>
 Performance_rating FLOAT </br>
 Relationship_satisfaction INT </br>
 Work_life_balance FLOAT</br>
 Distance_from_home FLOAT </br>

![TABLAS](https://github.com/s-armeni/proyecto-da-promo-H-modulo-3-team-3-DataMinds/blob/main/tablas_peoplemetrics.png)
