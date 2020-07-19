from Config import Config
import pyodbc

config = Config("config.ini")
table=input("Enter table name ")
column=input("Enter index coumn name ")

def connect(database:str):
    connection = pyodbc.connect("DRIVER="+config[database]["driver"]+";SERVER="+config[database]["server"]+";PORT=1433;DATABASE="+config[database]["database"]+";UID="+config[database]["username"]+";PWD=" + config[database]["password"])
    cursor = connection.cursor()
    return cursor

source_cursor=connect("source")

source_cursor.execute("SELECT " + column + " FROM dbo."+table)

for row in source_cursor:
    print(row)
