#!C:\\Program Files\\Python\\pythonw.exe
import cgi
import otchet 

form = cgi.FieldStorage()
database_name = form.getfirst("database", "не задано")
table_name = form.getfirst("table_name", "не задано")
name = form.getfirst("name", "не задано")
field_stud = form.getfirst("field_stud", "не задано")
department = form.getfirst("department", "не задано") 

driver = 'MySQL ODBC 8.0 ANSI Driver'
server = 'localhost'
user = 'root'
password = 'root'
path_to_save = 'D:/Студенты/'


    
conn_str = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database_name};'
        f'UID={user};'
        f'PWD={password};'
        'charset=utf8mb4;'
    )
    

result = otchet.save_data_to_db(conn_str, table_name,  name=name, field_stud=field_stud,department=department)

print("Content-type: text/html\n\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Processing data!</h1>")
print("<p>query: {}</p>".format(result))

print("""</body>
        </html>""")
