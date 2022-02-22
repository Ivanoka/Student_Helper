import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import configparser

config = configparser.ConfigParser()
config.read('.\config\settings.ini')

bot_session = vk_api.VkApi(token = config["CONNECTION"]["TOKEN"])
group_id = config["CONNECTION"]["GROUP_ID"]
vk = bot_session.get_api()


def LongPollListen():
    longpoll = VkBotLongPoll(bot_session, group_id)
    for event in longpoll.listen():
            return event
        
class MessangeSend():
    def User(user_id, message):
        vk.messages.send(key = config["CONNECTION"]["KEY"], 
                        server = config["CONNECTION"]["SERVER"], 
                        ts = config["CONNECTION"]["TS"], 
                        user_id = user_id, 
                        random_id = get_random_id(), 
                        message = message)
        
    def Chat(chat_id, message):
        vk.messages.send(key = config["CONNECTION"]["KEY"], 
                        server = config["CONNECTION"]["SERVER"], 
                        ts = config["CONNECTION"]["TS"], 
                        chat_id = chat_id, 
                        random_id = get_random_id(), 
                        message = message)
