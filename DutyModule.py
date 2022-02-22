import lib.vk_api_functions as vk_api_functions

def DutyModuleMain():
    while True:
        event = vk_api_functions.LongPollListen()
        print(event) 