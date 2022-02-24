import sys
import subprocess
import lib.vkApiFunctions as VkApiFuntions



subprocess.Popen([sys.executable, 'dutyModule.py'])

while True:
    event = VkApiFuntions.LongPollListen()
    try:
        if event.message.text == "/start" or event.message.action["type"] == "chat_invite_user":
            subprocess.Popen([sys.executable, 'chatRegistration.py', str(event.message.peer_id)])
    except:
        pass