import pyodbc
from datetime import datetime
from typing import List, Set

def get_data_from_db(conn_str:str, table_name:str, query:str):
    '''
    Return rows and columns name satisfying the request

    :param conn_str: - setting for connection to db
    :param table_name: - name of table
    :param query: - query to db
    :return: - rows and col names from db
    '''
    col_names:List[str] = []
    
    cnxn: pyodbc.Connection = pyodbc.connect(conn_str)
    cursor: pyodbc.Cursor = cnxn.cursor()
    
    cursor.execute(query)
    rows: List[pyodbc.Rows] = cursor.fetchall()
    
    for column_desc in rows[0].cursor_description:
        col_names.append(str(column_desc[0]))
    return rows, col_names

def save_data_to_db(conn_str:str, table_name:str, **fields:dict):
    '''
    Insert data into db table

    :param conn_str: - setting for connection to db
    :param table_name: - name of table
    :param fields: - dict with database values
    :return: - Inserted message
    '''
    inserted_values: str = 'NULL,' + ','.join(map(lambda param: "'" + str(param) + "'", fields.values()))
    template_query: str = f'INSERT INTO {table_name} VALUES({inserted_values});'
    cnxn: pyodbc.Connection = pyodbc.connect(conn_str)
    cursor: pyodbc.Cursor = cnxn.cursor()
    cursor.execute(template_query)
    cursor.commit()
    return 'Inserted'

def save_table_in_file(path:str, table_name:str,
                       col_names:List[str],
                       table_rows:List[str]):
    '''
    Save data from table in html file

    :param path: - path to save file
    :param table_name: - name of table
    :param col_names: - name of table columns
    :param table_rows: - rows from db
    :return: - name of saved html file
    '''
    HTML_TEMPLATE = '''<h1 style="text-align:center;">Отчёт по таблице {0}</h1>
                       <table cellspacing="2" border="1" style="width:100%;"><tr>'''
    suffix: str = '_otchet.html'
    current_date: str = str(datetime.now().date())
    file_name: str = f'{path}{table_name}{current_date}{suffix}'
    
    with open(file_name, 'w') as file:
        file.write(HTML_TEMPLATE.format(table_name))
        
        for column_name in col_names:
            file.write(f'<th>{column_name}</th>')
        file.write('</tr>')
        
        for row in table_rows:
            file.write('<tr>')
            for col in row:
                file.write(f'<td>{col}</td>\n')
                
        file.write('<h2>' + datetime.now().strftime("%d/%m/%Y %H:%M") + '</h2>')
        return file_name


    
def main():
    database_name = 'egu'
    driver = 'MySQL ODBC 8.0 ANSI Driver'
    server = 'localhost'
    user = 'root'
    password = 'root'
    table_name = 'cost'
    path_to_save = 'D:/Студенты/'

    #database_name = input('Database name: ')
    #table_name = input('Table name: ')
    
    query = f'select metr, type from {table_name}'
    
    conn_str = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database_name};'
        f'UID={user};'
        f'PWD={password};'
        'charset=utf8mb4;'
    )
    
    rows, col_names = get_data_from_db(conn_str, table_name, query)
    print('Saved to: ',save_table_in_file(path_to_save, table_name, col_names, rows))
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
