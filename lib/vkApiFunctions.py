import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
import json


def RemoveChatBot(chatId):
    with open('.\config\settings.json', 'r', encoding='utf-8') as json_cfg:
        config = json.load(json_cfg)
    bot_session = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
    vk = bot_session.get_api()
    vk.messages.removeChatUser(chat_id = chatId, member_id = -(config["CONNECTION"]["GROUPID"]))

def LongPollListen():
    with open('.\config\settings.json', 'r', encoding='utf-8') as json_cfg:
        config = json.load(json_cfg)
    bot_session = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
    group_id = config["CONNECTION"]["GROUPID"]
    vk = bot_session.get_api()
    longpoll = VkBotLongPoll(bot_session, group_id)
    for event in longpoll.listen():
            return event
        
class MessangeSend():
    def User(user_id, message):
        with open('.\config\settings.json', 'r', encoding='utf-8') as json_cfg:
            config = json.load(json_cfg)
        bot_session = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
        vk = bot_session.get_api()
        vk.messages.send(key = config["CONNECTION"]["KEY"], 
                        server = config["CONNECTION"]["SERVER"], 
                        ts = config["CONNECTION"]["TS"], 
                        user_id = user_id, 
                        random_id = get_random_id(), 
                        message = message)
        
    def Chat(chat_id, message):
        with open('.\config\settings.json', 'r', encoding='utf-8') as json_cfg:
            config = json.load(json_cfg)
        bot_session = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
        vk = bot_session.get_api()
        vk.messages.send(key = config["CONNECTION"]["KEY"], 
                        server = config["CONNECTION"]["SERVER"], 
                        ts = config["CONNECTION"]["TS"], 
                        chat_id = chat_id, 
                        random_id = get_random_id(), 
                        message = message)



if __name__ == "__main__":
    pass