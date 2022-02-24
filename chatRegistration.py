import lib.vkApiFunctions as VkApiFuntions
import sqlite3
import sys
import json
from datetime import datetime, timedelta


timeIsOver = 5
timeNow = datetime.now()
peerId = int(sys.argv[1])
sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()
chatId = peerId - 2000000000


with open('config\message_text.json', 'r', encoding='utf-8') as message:
    message = json.load(message)
VkApiFuntions.MessangeSend.Chat(peerId - 2000000000, message["chatRegistration"]["chatConnection"])
sqlCursor.execute("SELECT GROUPNUMBER FROM GROUPS WHERE VKID IS NULL")
groupsNumder = sqlCursor.fetchone()
flag = True
while flag:
    event = VkApiFuntions.LongPollListen()
    if event.message.peer_id == peerId:
        checkFlag = True
        if (datetime.now() - timeNow) < timedelta(minutes = timeIsOver):
            print(datetime.now() - timeNow)
            for number in groupsNumder:
                print(number)
                if event.message.text == str(number):
                    with open('config\message_text.json', 'r', encoding='utf-8') as message:
                        message = json.load(message)
                    VkApiFuntions.MessangeSend.Chat(chatId, (message["chatRegistration"]["groupRegistration"]).format(number))
                    sqlCursor.execute("UPDATE GROUPS SET VKID = {} WHERE GROUPNUMBER = {}".format(chatId, number))
                    sqlConnection.commit()
                    checkFlag, flag = False, False
            if checkFlag:
                with open('config\message_text.json', 'r', encoding='utf-8') as message:
                    message = json.load(message)
                VkApiFuntions.MessangeSend.Chat(chatId, message["chatRegistration"]["groupNotFound"])
        else:
            with open('config\message_text.json', 'r', encoding='utf-8') as message:
                message = json.load(message)
            VkApiFuntions.MessangeSend.Chat(chatId, message["chatRegistration"]["timeIsOver"])
            flag = False