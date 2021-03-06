import requests
import json
from time import sleep



while True:
    with open('config\settings.json', 'r', encoding='utf-8') as config:
        newConfig = json.load(config)
    newConnectionData = requests.get('https://api.vk.com/method/messages.getLongPollServer', 
                             params={'access_token': newConfig["CONNECTION"]["TOKEN"], 'v': 5.131}).json()
    if "error" in newConnectionData:
        print(newConnectionData)
    else:
        if newConfig["CONNECTION"]["SERVER"] != newConnectionData["response"]["server"]:
            newConfig["CONNECTION"]["SERVER"] = newConnectionData["response"]["server"]
            print("Update 'server' value")
        if newConfig["CONNECTION"]["KEY"] != newConnectionData["response"]["key"]:
            newConfig["CONNECTION"]["KEY"] = newConnectionData["response"]["key"]
            print("Update 'key' value")
        if newConfig["CONNECTION"]["TS"] != newConnectionData["response"]["ts"]:
            newConfig["CONNECTION"]["TS"] = newConnectionData["response"]["ts"]
            print("Update 'ts' value")
        with open('config\settings.json', 'w', encoding='utf-8') as config:
            json.dump(newConfig, config, ensure_ascii=False, indent=4)
    sleep(3600)