from time import sleep
import json
from dutyModule import DutyModuleMain

while True:
    DutyModuleMain()

    with open('config\settings.json', 'r', encoding='utf-8') as config:
        config = json.load(config)
        sleep(int(config["TIME_SLEEP"]))