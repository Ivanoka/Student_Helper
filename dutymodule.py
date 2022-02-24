from datetime import datetime
from datetime import date
from time import sleep
import json
import sqlite3
import lib.vk_api_functions as VkApiFunctions


sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()



def SelectionNewDuty(numberGroup):
    flag = True

    sqlCursor.execute("SELECT COUNT(*) FROM '" + str(numberGroup) + "'")
    countId = sqlCursor.fetchone()
    countId = countId[0]
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
            newDuty = (newDuty % countId) + 1
            
def SelectionLastDuty(numberGroup, idDuty):
    flag = True
    
    sqlCursor.execute("SELECT COUNT(*) FROM '" + str(numberGroup) + "'")
    countId = sqlCursor.fetchone()
    countId = countId[0]
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
            idDuty = (idDuty % countId) + 1
    
    


def DutyModuleMain():
    while True:
        print(date.today().weekday())
        with open('config\duty_notification_settings.json', 'r', encoding='utf-8') as dutyNotifSend:
                config = json.load(dutyNotifSend)
        sqlCursor.execute("SELECT GROUPNUMBER FROM GROUPS WHERE DUTYENABLE = 1")
        groups = sqlCursor.fetchone()
        if groups == None:
            with open('config\settings.json', 'r', encoding='utf-8') as config:
                config = json.load(config)
                sleep(int(config["TIME_SLEEP"]))
        else:
            for numberGroup in groups:
                with open('config\duty_notification_settings.json', 'r', encoding='utf-8') as dutyNotifSend:
                    config = json.load(dutyNotifSend)
                if config[str(numberGroup)][str(date.today().weekday())]["SENDFLAG"]:
                    if config[str(numberGroup)][str(date.today().weekday())]["TIMESEND"] == (datetime.now()).strftime('%H:%M'):
                        sqlCursor.execute("SELECT ID FROM '" + str(numberGroup) + "' WHERE LASTONDUTY = 1")
                        idDuty = sqlCursor.fetchone()
                        if idDuty == None:
                            SelectionNewDuty(numberGroup)
                            with open('config\settings.json', 'r', encoding='utf-8') as config:
                                config = json.load(config)
                                sleep(int(config["TIME_SLEEP"]))
                        else:
                            SelectionLastDuty(numberGroup, idDuty[0])
                            with open('config\settings.json', 'r', encoding='utf-8') as config:
                                config = json.load(config)
                                sleep(int(config["TIME_SLEEP"]))
                    else:
                        with open('config\settings.json', 'r', encoding='utf-8') as config:
                            config = json.load(config)
                            sleep(int(config["TIME_SLEEP"]))
                else:
                    with open('config\settings.json', 'r', encoding='utf-8') as config:
                        config = json.load(config)
                        sleep(int(config["TIME_SLEEP"]))

DutyModuleMain()