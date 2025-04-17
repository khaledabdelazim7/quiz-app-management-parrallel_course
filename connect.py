import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'BISHO\SQLEXPRESS' 
DATABASE_NAME = 'quiz_app'

connection_string =f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection = yes;
""" 
conn = odbc.connect(connection_string)
cursor = conn.cursor()
print(conn)



