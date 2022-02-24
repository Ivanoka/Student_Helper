import lib.vk_api_functions as VkApiFuntions
import sqlite3


sqlConnection = sqlite3.connect('db\database.db')
sqlCursor = sqlConnection.cursor()



while True:
    event = VkApiFuntions.LongPollListen()
    try:
        if event.message.action["type"] == "chat_invite_user":
            VkApiFuntions.MessangeSend.Chat(event.message.peer_id - 2000000000, "Чтобы начать назначьте Бота администратором беседы и напишите номер группы.")
            sqlCursor.execute("SELECT GROUPNUMBER FROM GROUPS WHERE VKID IS NULL")
            groupsNumder = sqlCursor.fetchone()
            peerId = event.message.peer_id
            flag = True
            while flag:
                event = VkApiFuntions.LongPollListen()
                if event.message.peer_id == peerId:
                    checkFlag = True
                    for number in groupsNumder:
                        print(number)
                        if event.message.text == str(number):
                            VkApiFuntions.MessangeSend.Chat(peerId - 2000000000, "Группа " + str(number) + " зарегистрирована")
                            checkFlag, flag = False, False
                    if checkFlag: 
                        VkApiFuntions.MessangeSend.Chat(peerId - 2000000000, "Номер группы не найден, попробуйте заново.")
    except:
        pass