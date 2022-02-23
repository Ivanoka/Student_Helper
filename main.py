import asyncio
import sqlite3
from dutymodule import DutyModuleMain


"""if __name__ == "__main__":
    asyncio.run(DutyModuleMain())"""
    
sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()

sqlCursor.execute("UPDATE '5142211' SET LASTONDUTY = 1 WHERE ID = 2")
sqlConnection.commit
sqlCursor.close()