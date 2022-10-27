'''
Gear Generator MAS417 Project
Flexible Production
ApiLibary
Martin Økter
25.10.2022
'''


import userapi
import first_class

action = True

uApi = userapi.UserApi()
testPrtin = first_class.testClass()


while True:

    while action:
        action = uApi.userInput()

    action = True

    testPrtin.retriveList(uApi)

    while action:
        action = uApi.fetchingTemperature()

