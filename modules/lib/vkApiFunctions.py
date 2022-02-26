import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
import json



def LongPollListen():
    with open('config\settings.json', 'r', encoding='utf-8') as config:
        config = json.load(config)
    botSession = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
    groupId = config["CONNECTION"]["GROUPID"]
    vk = botSession.get_api()
    longpoll = VkBotLongPoll(botSession, groupId)
    for event in longpoll.listen():
            return event
        
class MessangeSend():
    def User(userId, message):
        with open('config\settings.json', 'r', encoding='utf-8') as config:
            config = json.load(config)
        botSession = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
        vk = botSession.get_api()
        vk.messages.send(key = config["CONNECTION"]["KEY"], 
                         server = config["CONNECTION"]["SERVER"], 
                         ts = config["CONNECTION"]["TS"], 
                         user_id = userId, 
                         random_id = get_random_id(), 
                         message = message)
        
    def Chat(chatId, message):
        with open('config\settings.json', 'r', encoding='utf-8') as config:
            config = json.load(config)
        botSession = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
        vk = botSession.get_api()
        vk.messages.send(key = config["CONNECTION"]["KEY"], 
                         server = config["CONNECTION"]["SERVER"], 
                         ts = config["CONNECTION"]["TS"], 
                         chat_id = chatId, 
                         random_id = get_random_id(), 
                         message = message)