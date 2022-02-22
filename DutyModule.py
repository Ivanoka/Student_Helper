import Lib.VkApiFunctions as VkApiFunctions

def DutyModuleMain():
    while True:
        event = VkApiFunctions.LongPollListen()
        print(event) 