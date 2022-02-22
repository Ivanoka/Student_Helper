import time
from datetime import datetime
from datetime import date
import json
import sqlite3
import lib.vk_api_functions as vk_api_functions


sql_connection = sqlite3.connect('.\db\database.db')
sql_cursor = sql_connection.cursor()
sql_cursor.execute('SELECT name from sqlite_master where type = "table"')
print(sql_cursor.fetchall()[0][0])


def SendNotification():
    with open('.\config\duty_notification_setings.json', 'r', encoding='utf-8') as json_cfg:
        config = json.load(json_cfg)
    if config["5142211"][str((date.today()).weekday())]["SENDFLAG"]:
        if config["5142211"][str((date.today()).weekday())]["TIMESEND"] == (datetime.now()).strftime('%H:%M'):
            vk_api_functions.MessangeSend.Chat(2000000002, "СЕГОДНЯ СУЧКИ МЫ БУДЕМ ЕБАТЬСЯ ДОЛГО И ПЛОТНО")
            time.sleep(10)
        else:
            time.sleep(10)
    else:
        time.sleep(10)



def DutyModuleMain():
    while True:
        SendNotification()