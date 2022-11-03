'''
Gear Generator MAS417 Project
Flexible Production
Main class
Martin Økter, Per Henrik, Torbjørn
28.10.2022
'''

import userapi
import pointgenerator as pg
import matplotlib.pyplot as plt

uApi = userapi.UserApi()

class GearGenerator:
    def __init__(self):
        self.next = 0
        self.spesificationList = []
        self.temp = 0
        self.pointsInner = []

    def inputFase(self):
        action = uApi.userInput()
        if action:
            self.spesificationList = uApi.getList()
            self.next += 1
        return 0

    def meshFase(self):
        action = uApi.generatingPMS(self.temp)
        action = True
    # HER PLOTTER JEG BARE FOR Å VISUALISERE FOR GØY
        ax = plt.axes(projection='3d')
        plt.plot(self.pGen.pointsInner[0],self.pGen.pointsInner[1],self.pGen.pointsInner[2], '*')
        plt.plot(self.pGen.xMain, self.pGen.yMain, self.pGen.zMain, '*')
        plt.plot(self.pGen.xOuter, self.pGen.yOuter, self.pGen.zOuter, '*')

        plt.plot(self.pGen.xInnerOffset, self.pGen.yInnerOffset, self.pGen.zInnerOffset, '*')
        plt.plot(self.pGen.xMainOffset, self.pGen.yMainOffset, self.pGen.zMainOffset, '*')
        plt.plot(self.pGen.xOuterOffset, self.pGen.yOuterOffset, self.pGen.zOuterOffset, '*')
        plt.show()

        # Sett inn meshing her
        # Torbjørn
        #bruk selp.pGen.gETpOINTS

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
        self.pGen = pg.PointGenerator(self.spesificationList) #Her oprettes objektet
        self.temp = self.pGen.returnTemp()
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
