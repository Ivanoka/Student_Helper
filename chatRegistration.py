import lib.vkApiFunctions as VkApiFuntions
import sqlite3
import sys
import json
from time import sleep
from datetime import datetime, timedelta


peerId = int(sys.argv[1])
chatId = peerId - 2000000000
timeIsOver = 5
timeNow = datetime.now()
with open('config\message_text.json', 'r', encoding='utf-8') as config:
    countOfTry = (json.load(config))["COUNTOFTRY"]
sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()


#ОБРАБОТКА ОШИБОК
def errorMessage(i):
    if i == 99:
        with open('config\message_text.json', 'r', encoding='utf-8') as message:
            VkApiFuntions.MessangeSend.Chat(chatId, (json.load(message))["chatRegistration"]["errorMessage"])
        sys.exit()

#ПОЛУЧЕНИЕ ИНФОРМАЦИИ ОТ ГРУППАХ
for i in range(countOfTry):
    errorMessage(i)
    try:
        sqlCursor.execute("SELECT GROUPNUMBER, VKID, AUTHORIZATIONCODE FROM GROUPS")
        groupIdCode = sqlCursor.fetchall()
        break
    except:
        sleep(0.1)
        continue

#ГРУППА УЖЕ ЗАРЕГЕСТРИРОВАНА
for id in groupIdCode:
    if chatId == id[1]:
        with open('config\message_text.json', 'r', encoding='utf-8') as message:
            VkApiFuntions.MessangeSend.Chat(chatId, ((json.load(message))["chatRegistration"]["groupIsAlreadyRegistered"]).format(id[0]))
        sys.exit()

#НЕТ ГРУПП ДЛЯ РЕГИСТРАЦИИ
noGrToReg = True
for id in groupIdCode:
    if id[1] == None: noGrToReg = False
if noGrToReg: 
    with open('config\message_text.json', 'r', encoding='utf-8') as message:
        VkApiFuntions.MessangeSend.Chat(chatId, (json.load(message))["chatRegistration"]["noGroupsToRegister"])
    sys.exit()

#РЕГИСТАРАЦИЯ БЕСЕДЫ
with open('config\message_text.json', 'r', encoding='utf-8') as message:
    VkApiFuntions.MessangeSend.Chat(chatId, (json.load(message))["chatRegistration"]["chatConnection"])
while True:
    event = VkApiFuntions.LongPollListen()
    if event.message.peer_id == peerId:
        if (datetime.now() - timeNow) < timedelta(minutes = timeIsOver):
            print(datetime.now() - timeNow)
            for code in groupIdCode:
                if event.message.text == code[2]:
                    for i in range(countOfTry):
                        errorMessage(i)
                        try:
                            sqlCursor.execute("SELECT VKID FROM GROUPS WHERE GROUPNUMBER = {}".format(code[0]))
                            oldVkId = sqlCursor.fetchone()
                            sqlCursor.execute("UPDATE GROUPS SET VKID = {} WHERE GROUPNUMBER = {}".format(chatId, code[0]))
                            sqlConnection.commit()
                            sqlCursor.execute("UPDATE GROUPS SET AUTHORIZATIONCODE = NULL WHERE GROUPNUMBER = {}".format(code[0]))
                            sqlConnection.commit()
                            break
                        except: continue
                    try:
                        if oldVkId != None:
                            with open('config\message_text.json', 'r', encoding='utf-8') as message:
                                VkApiFuntions.MessangeSend.Chat(oldVkId, ((json.load(message))["chatRegistration"]["disconnectOldChat"]).format(code[0]))
                    except: pass
                    with open('config\message_text.json', 'r', encoding='utf-8') as message:
                        VkApiFuntions.MessangeSend.Chat(chatId, ((json.load(message))["chatRegistration"]["groupRegistration"]).format(code[0]))
                    sys.exit()
            with open('config\message_text.json', 'r', encoding='utf-8') as message:
                VkApiFuntions.MessangeSend.Chat(chatId, (json.load(message))["chatRegistration"]["errorCode"])
        else:
            with open('config\message_text.json', 'r', encoding='utf-8') as message:
                VkApiFuntions.MessangeSend.Chat(chatId, (json.load(message))["chatRegistration"]["timeIsOver"])
            sys.exit()