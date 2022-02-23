import time
from datetime import datetime
from datetime import date
import json
import sqlite3
import lib.vk_api_functions as VkApiFunctions

sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()



def SelectionNewDuty(numberGroup):
    flag = True
    
    sqlCursor.execute("SELECT COUNT(*) FROM '" + str(numberGroup) + "'")
    countId = sqlCursor.fetchall()
    countId = countId[0][0]
    newDuty = (date.today()).day % countId
    print(newDuty)
    while flag:
        sqlCursor.execute("SELECT SICK FROM  '" + str(numberGroup) + "' WHERE ID = " + str(newDuty))
        newDutySick = sqlCursor.fetchone()
        newDutySick = newDutySick[0]
        if newDutySick == 0:
            sqlCursor.execute("UPDATE '" + str(numberGroup) + "' SET LASTONDUTY = 1 WHERE ID = " + str(newDuty))
            sqlConnection.commit
            print("Дежурный выбран")
            flag = False


def DutyModuleMain():
    while True:
        print(date.today().weekday())
        with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as dutyNotifSend:
                config = json.load(dutyNotifSend)
        sqlCursor.execute("SELECT GROUPNUMBER FROM GROUPS WHERE DUTYENABLE = 1")
        groups = sqlCursor.fetchall()
        if groups == None:
            time.sleep(10)
        else:
            for numberGroup in groups:
                with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as dutyNotifSend:
                    config = json.load(dutyNotifSend)
                if config[str(numberGroup[0])][str(date.today().weekday())]["SENDFLAG"]:
                    if config[str(numberGroup[0])][str(date.today().weekday())]["TIMESEND"] == (datetime.now()).strftime('%H:%M'):
                        sqlCursor.execute("SELECT ID FROM '" + str(numberGroup[0]) + "' WHERE LASTONDUTY = 1")
                        idDuty = sqlCursor.fetchone()
                        if idDuty == None:
                            SelectionNewDuty(numberGroup[0])
                            time.sleep(10)
                        else:
                            time.sleep(10)     
                    else:
                        time.sleep(10)
                else:
                    time.sleep(10)