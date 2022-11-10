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


class GearGenerator:
    def __init__(self):
        self.next = 0
        self.spesificationList = [10, 40, 2,  2, 20, 200, 8.3540, 58.2250]
        self.temp = 0
        self.pointsInner = []

        self.mg = meshgenerator.MeshGenerator()
        self.uApi = userapi.UserApi()

    def inputFase(self):
        '''
        Fase for reciving user input for wanted size of the gear
        '''
        action = self.uApi.userInput()
        if action:
            midleList = self.uApi.getList()
            if midleList[4] != 0:
                self.spesificationList = uApi.getList()
            self.next += 1
        return 0

    def meshFase(self):
        '''
        Fase for creating a mesh from the reciving point cloud and save as .stl file
        '''
        action = self.uApi.generatingPMS(self.temp)
        action = True

        #Import Points from point generator
        pointsInner = self.pGen.getPointsInner()
        pointsMain = self.pGen.getPointsMain()
        pointsOuter =  self.pGen.getPointsOuter()
        pointsInnerOffset = self.pGen.getPointsInnerOffset()
        pointsMainOffset = self.pGen.getPointsMainOffset()
        pointsOuterOffset =  self.pGen.getPointsOuterOffset()

        self.mg.inputAndRun(pointsInner, pointsMain, pointsOuter, pointsInnerOffset, pointsMainOffset, pointsOuterOffset, self.spesificationList[1])
        self.mg.faceGenerator()
        self.mg.plotMesh()
        self.mg.generateSTL()

        if action:
            self.next += 1
        return 0

    def outputFase(self):
        '''
        Feedback for succsesfull gear generating and usefull information
        '''
        action = self.uApi.outputPage()
        if action:
            self.next = 0
        return 0

    def pointFase(self):
        '''
        Fase for genrerating th epointcloud from the user data and preset parameters
        '''
        # Keyword if loop shal be used
        action = True

        #Rertriving location mean temperature
        self.uApi.fetchingTemperature()
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
        self.pGen = pg.PointGenerator(self.spesificationList) #Her oprettes objektet, bytt til spesification list når den skal testes skikkelig.
        self.temp = self.pGen.returnTemp()
        # Per
        if action:
            self.next += 1
        return 0

    def mainLoop(self):
        '''
        Main loop for selection of fase and corensponding fase
        '''
        if self.next == 0:
            self.inputFase()
        elif self.next == 1:
            self.pointFase()
        elif self.next == 2:
            self.meshFase()
        elif self.next == 3:
            self.outputFase()
