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
import meshgenerator

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

        #Import Points from point generator
        pointsInner = self.pGen.getPointsInner()
        pointsMain = self.pGen.getPointsMain()
        pointsOuter =  self.pGen.getPointsOuter()
        pointsInnerOffset = self.pGen.getPointsInnerOffset()
        pointsMainOffset = self.pGen.getPointsMainOffset()
        pointsOuterOffset =  self.pGen.getPointsOuterOffset()

        mg = meshgenerator.MeshGenerator(pointsInner, pointsMain, pointsOuter, pointsInnerOffset, pointsMainOffset, pointsOuterOffset, self.spesificationList[1])



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
        dummyList = [10, 40, 2,  2, 20, 200,8.3540, 58.2250]
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
        self.pGen = pg.PointGenerator(dummyList) #Her oprettes objektet, bytt til spesification list når den skal testes skikkelig.
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
