import time
from datetime import datetime
from datetime import date
import json
import sqlite3
import lib.vk_api_functions as VkApiFunctions

timeSleep = 10
sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()



def SelectionNewDuty(numberGroup):
    flag = True

    sqlCursor.execute("SELECT COUNT(*) FROM '" + str(numberGroup) + "'")
    countId = sqlCursor.fetchone()
    countId = countId[0] - 1
    newDuty = (date.today()).day % countId + 1
    while flag:
        sqlCursor.execute("SELECT SICK, WASONDUTY FROM  '" + str(numberGroup) + "' WHERE ID = " + str(newDuty))
        newDutySick = sqlCursor.fetchone()
        if newDutySick[0] == 0 and newDutySick[1] == 0:
            sqlCursor.execute("UPDATE '" + str(numberGroup) + "' SET LASTONDUTY = 1 WHERE ID = " + str(newDuty))
            sqlConnection.commit()
            print("Дежурный выбран") #######################
            flag = False
        else:
            newDuty = (newDuty + 1) % (date.today()).day

def SelectionLastDuty(numberGroup, idDuty):
    flag = True
    
    while flag:
        sqlCursor.execute("SELECT SICK, WASONDUTY FROM  '" + str(numberGroup) + "' WHERE ID = " + str(idDuty))
        dutySick = sqlCursor.fetchone()
        if dutySick[0] == 0 and dutySick[1] == 0:
            sqlCursor.execute("SELECT SENDDUTYFLAG FROM '" + str(numberGroup) + "' WHERE ID = " + str(idDuty))
            sendFlag = sqlCursor.fetchone()
            if sendFlag[0] == 0:
                print("Страый дежурный назначен") #########################
                sqlCursor.execute("UPDATE '" + str(numberGroup) + "' SET SENDDUTYFLAG = 1 WHERE ID = " + str(idDuty))
                sqlConnection.commit()
            else:
                flag = False
        else:
            idDuty = (idDuty + 1) % (date.today()).day



def DutyModuleMain():
    while True:
        print(date.today().weekday())
        with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as dutyNotifSend:
                config = json.load(dutyNotifSend)
        sqlCursor.execute("SELECT GROUPNUMBER FROM GROUPS WHERE DUTYENABLE = 1")
        groups = sqlCursor.fetchone()
        if groups == None:
            time.sleep(timeSleep)
        else:
            for numberGroup in groups:
                with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as dutyNotifSend:
                    config = json.load(dutyNotifSend)
                if config[str(numberGroup)][str(date.today().weekday())]["SENDFLAG"]:
                    if config[str(numberGroup)][str(date.today().weekday())]["TIMESEND"] == (datetime.now()).strftime('%H:%M'):
                        sqlCursor.execute("SELECT ID FROM '" + str(numberGroup) + "' WHERE LASTONDUTY = 1")
                        idDuty = sqlCursor.fetchone()
                        if idDuty == None:
                            SelectionNewDuty(numberGroup)
                            time.sleep(timeSleep)
                        else:
                            SelectionLastDuty(numberGroup, idDuty[0])
                            time.sleep(timeSleep)     
                    else:
                        time.sleep(timeSleep)
                else:
                    time.sleep(timeSleep)