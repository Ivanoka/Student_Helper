import time
from datetime import datetime
from datetime import date
import json
import sqlite3
import lib.vk_api_functions as vk_api_functions

sqlConnection = sqlite3.connect('.\db\database.db')
sqlCursor = sqlConnection.cursor()



def SendNotification():
    with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as dutyNotifSend:
                config = json.load(dutyNotifSend)
    sqlCursor.execute("SELECT * FROM GROUPS WHERE DUTYENABLE = 1")
    groups = sqlCursor.fetchall()
    if groups == None:
        time.sleep(10)
    else:
        for numberGroup in groups:
            with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as dutyNotifSend:
                config = json.load(dutyNotifSend)
            if config[str(numberGroup[0])][str((date.today()).weekday())]["SENDFLAG"]:
                if config[str(numberGroup[0])][str((date.today()).weekday())]["TIMESEND"] == (datetime.now()).strftime('%H:%M'):
                    vk_api_functions.MessangeSend.Chat(2, "СЕГОДНЯ СУЧКИ МЫ БУДЕМ ЕБАТЬСЯ ДОЛГО И ПЛОТНО")
                    time.sleep(10)
                else:
                    time.sleep(10)
            else:
                time.sleep(10)



def DutyModuleMain():
    while True:
        SendNotification()