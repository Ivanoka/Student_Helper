import sqlite3
import time

sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()

while True:
    sqlCursor.execute("SELECT SICK, WASONDUTY FROM  '5142211' WHERE ID = 1")
    print(sqlCursor.fetchone())
    time.sleep(3)