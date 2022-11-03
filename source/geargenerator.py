'''
Gear Generator MAS417 Project
Flexible Production
Main class
Martin Økter, Per Henrik, Torbjørn
28.10.2022
'''

import userapi

uApi = userapi.UserApi()


class GearGenerator:
    def __init__(self):
        self.next = 0
        self.spesificationList = []
        self.temp = 0

    def inputFase(self):
        action = uApi.userInput()
        if action:
            self.spesificationList = uApi.getList()
            self.next += 1
        return 0

    def meshFase(self):
        action = uApi.generatingPMS(self.temp)
        action = True

        # Sett inn meshing her
        # Torbjørn

        if action:
            self.next += 1
        return 0

    def outputFase(self):
        action = uApi.outputPage()
        if action:
            self.next = 0
        return 0

    def pointFase(self):
        uApi.fetchingTemperature()
        action = True

        # Sett inn point genrating her
        # Per

        if action:
            self.next += 1
        return 0

    def mainLoop(self):
        if self.next == 0:
            self.inputFase()
        elif self.next == 1:
            self.pointFase()
        elif self.next == 2:
            self.meshFase()
        elif self.next == 3:
            self.outputFase()