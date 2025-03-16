import mysql.connector
def init():
    cursor.execute("drop database if exists DBT25_A1_PES2UG22CS506_Sanket;")
    cursor.execute("create database DBT25_A1_PES2UG22CS506_Sanket;")
    cursor.execute("use DBT25_A1_PES2UG22CS506_Sanket;")
    cursor.execute("create table diagnosis (id int primary key,diagnosis varchar(50));")
    cursor.execute('create table medical_history(id int primary key,family_history enum("no","yes"),radiation_exposure enum("no","yes"),iodine_deficiency enum("no","yes"),smoking enum("no","yes"),obesity enum("no","yes"),diabetes enum("no","yes"));')
    cursor.execute('create table nodule_details(id int primary key,nodule_size float,thyroid_cancer_risk enum("low","medium","high"));')
    cursor.execute('create table patient(id int primary key,age int,gender enum("male","female"),country varchar(50),ethnicity varchar(50));')
    cursor.execute('create table thyroid_test_results(id int primary key,tsh_level float,t3_level float,t4_level float);')

def bulk_inserter(sql_file_path):
    with open(sql_file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    sql_queries = sql_script.split(';')
    for query in sql_queries:
        query = query.strip()
        if query:  
            try:
                cursor.execute(query)
                print(f"Executed query: {query}")
            except mysql.connector.Error as err:
                print(f"Error executing query: {query}\n{err}")

    print("\n",sql_file_path,"execution is successfull ")

con_init = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
sql_file_path1="sql/diagnosis_insert.sql"
sql_file_path2="sql/medical_history_insert.sql"
sql_file_path3="sql/nodule_details_insert.sql"
sql_file_path4="sql/patient_insert.sql"
sql_file_path5="sql/thyroid_test_results_insert.sql"
sql_file_path6="sql/rel.sql"

cursor = con_init.cursor()
init()
con_init.commit()
cursor.close()
con_init.close()
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="DBT25_A1_PES2UG22CS506_Sanket"
)
cursor=con.cursor()
bulk_inserter(sql_file_path1)
bulk_inserter(sql_file_path2)
bulk_inserter(sql_file_path3)
bulk_inserter(sql_file_path4)
bulk_inserter(sql_file_path5)
bulk_inserter(sql_file_path6)
con.commit()
cursor.close()
con.close()
