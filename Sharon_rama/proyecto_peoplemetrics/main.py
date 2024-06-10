# %%
import pandas as pd

from src import soporte_queries_creacion_bbdd as query
from src import bbdd_dataminds_soporte as bbdd
# %%
bbdd.create_bbdd(query.query_create_bbdd, "AlumnaAdalab")
# %%
bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_employees)
# %%
bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_job_details)
# %%
bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_employee_profile)
# %%
bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_salary)
# %%
bbdd.create_table("root", "AlumnaAdalab", "peoplemetrics", query.query_table_employee_company)
# %%
bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_employees, bbdd.data_employees)
# %%
bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_employee_profile,bbdd.data_employee_profile)
# %%
bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_job_details,bbdd.data_job_details)
# %%
bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_salary,bbdd.data_salary)
# %%
bbdd.insert_data('root', 'AlumnaAdalab', 'peoplemetrics',query.query_insert_data_employee_company,bbdd.data_employee_company)



