import sys
import json
import subprocess
from time import sleep
import modules.lib.vkApiFunctions as VkApiFuntions



#subprocess.Popen([sys.executable, 'modules\dutyModule.py'])

while True:
    try:
        event = VkApiFuntions.LongPollListen()
        with open('.\config\settings.json', 'r', encoding='utf-8') as json_cfg:
            group_id = (json.load(json_cfg))["CONNECTION"]["GROUPID"]
        if event.message.text == "/start":
            subprocess.Popen([sys.executable, 'modules\chatRegistration.py', str(event.message.peer_id)])
        elif event.message.action["type"] == "chat_invite_user" and event.message.action["member_id"] == -(int(group_id)):
            subprocess.Popen([sys.executable, 'modules\chatRegistration.py', str(event.message.peer_id)])
    except: continue