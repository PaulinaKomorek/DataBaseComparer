from Config import Config
import pyodbc

config = Config("config.ini")
table = input("Enter table name ")
column = input("Enter index coumn name ")


def connect(database: str):
    connection = pyodbc.connect("DRIVER="+config[database]["driver"]+";SERVER="+config[database]["server"]+";PORT=1433;DATABASE=" +
                                config[database]["database"]+";UID="+config[database]["username"]+";PWD=" + config[database]["password"])
    cursor = connection.cursor()
    return cursor


source_cursor = connect("source")
snapshot_cursor = connect("snapshot")

source_cursor.execute("SELECT " + column + " FROM dbo."+table)
snapshot_cursor.execute("SELECT " + column + " FROM dbo."+table)

source_indexes = set(map(lambda x: x[0], source_cursor))
snapshot_indexes = set(map(lambda x: x[0], snapshot_cursor))
source_diff = list(source_indexes-snapshot_indexes)
snapshot_diff = list(snapshot_indexes-source_indexes)
with open("source_diff.txt", "w") as sf:
    sf.write(", ".join(map(lambda x: str(x), source_diff)))
with open("snapshot_diff.txt", "w") as sf:
    sf.write(", ".join(map(lambda x: str(x), snapshot_diff)))
print("There are " + str(len(source_diff)) +
      " rows which are in source database, but in snapshot database.")
print("There are " + str(len(snapshot_diff)) +
      " rows which are in snapshot database, but in source database.")
