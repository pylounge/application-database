#!C:\\Program Files\\Python\\pythonw.exe
import cgi
import otchet 

form = cgi.FieldStorage()
query = form.getfirst("query", "не задано")
database_name = form.getfirst("database", "не задано")
table_name = form.getfirst("table_name", "не задано")

driver = 'MySQL ODBC 8.0 ANSI Driver'
server = 'localhost'
user = 'root'
password = 'root'
path_to_save = 'D:/Студенты/'

#database_name = input('Database name: ')
#table_name = input('Table name: ')
    
query = f'{query}{table_name}'
    
conn_str = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database_name};'
        f'UID={user};'
        f'PWD={password};'
        'charset=utf8mb4;'
    )
    
rows, col_names = otchet.get_data_from_db(conn_str, table_name, query)
result = 'Saved to: ', otchet.save_table_in_file(path_to_save, table_name, col_names, rows)

print("Content-type: text/html\n")
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