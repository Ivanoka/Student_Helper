import lib.vk_api_functions as VkApiFuntions
import sqlite3
import sys

peerId = int(sys.argv[1])
sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()



VkApiFuntions.MessangeSend.Chat(peerId - 2000000000, "Вы подключили Помошника студента в вашу бесседу.\nДля регистрации назначьте нас Администратором и напишите номер группы\nДля регестрации у вас есть 5 минут.")
sqlCursor.execute("SELECT GROUPNUMBER FROM GROUPS WHERE VKID IS NULL")
groupsNumder = sqlCursor.fetchone()
flag = True
while flag:
    event = VkApiFuntions.LongPollListen()
    if event.message.peer_id == peerId:
        checkFlag = True
        for number in groupsNumder:
            print(number)
            if event.message.text == str(number):
                VkApiFuntions.MessangeSend.Chat(peerId - 2000000000, f"Группа {number} зарегистрирована")
                checkFlag, flag = False, False
        if checkFlag: 
            VkApiFuntions.MessangeSend.Chat(peerId - 2000000000, "Номер группы не найден, попробуйте заново.")
