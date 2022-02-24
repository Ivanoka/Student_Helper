import sys
import subprocess
import lib.vk_api_functions as VkApiFuntions


subprocess.Popen([sys.executable, 'dutyModule.py'])

while True:
    event = VkApiFuntions.LongPollListen()
    try:
        if event.message.action["type"] == "chat_invite_user":
            subprocess.Popen([sys.executable, 'chatRegistration.py', str(event.message.peer_id)])
    except:
        pass