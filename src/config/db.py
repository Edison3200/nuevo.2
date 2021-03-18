import mariadb


config = {
    'host':'localhost',
    'port':3308,
    'user':'root',
    'password':'',
    'database':'tienda'
}
try:
    DB = mariadb.connect(**config)
    DB.autocommit = True
except:
    DB = False
    print("error al conectarse a la base de datos")
    
def instalarDB():
    file_sql = open(SQL_PATH, 'r')
    sql = file_sql.read()

    cursor = DB.cursor()

    sqlCommands = sql.split(';')
    
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except:
            print ("Saltando comando")

    cursor.close()