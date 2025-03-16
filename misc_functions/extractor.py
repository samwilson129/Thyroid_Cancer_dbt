import mysql.connector
import csv

host = "localhost"
user = "root"
password = "root"
database = "thyroid_cancer"

file_path = "thyroid_test_results_table.csv"
table_name = "thyroid_test_results"
field_delimiter = ","
line_delimiter = "\n"

insert_file_path = "insert_statements.txt"
insert_file = open(insert_file_path, "w")

con = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = con.cursor()


columns = ["id","tsh_level","t3_level","t4_level"]   


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=field_delimiter)
    next(csv_reader) #to skip header rows
    for row in csv_reader:
        # Ensure the number of columns in the CSV matches the number of table columns
        if len(row) == len(columns):
            # Generate the INSERT statement with columns explicitly listed
            insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join([repr(value) for value in row])});"
            # Execute the INSERT statement in the database
            try:
                cursor.execute(insert_query)
                # Write the INSERT statement to the file
                insert_file.write(insert_query + "\n")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
        
        else:
            print(f"Skipping row with incorrect number of columns: {row}")

con.commit()
cursor.execute(f"SELECT COUNT(*) AS total_rows FROM {table_name}")
result = cursor.fetchone()
total_rows = result[0]
print(f"{total_rows} rows have been added to the table {table_name}")
insert_file.close()
cursor.close()
con.close()
