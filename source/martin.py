'''
Gear Generator MAS417 Project
Flexible Production
ApiLibary
Martin Økter
25.10.2022
'''


import userapi

action = True

uApi = userapi.UserApi()


while True:

    while action:
        action = uApi.userInput()

    action = True
    while action:
        action = uApi.fetchingTemperature()

