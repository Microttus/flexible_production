'''
Gear Generator MAS417 Project
Flexible Production
Main class
Martin Økter, Per Henrik, Torbjørn
28.10.2022
'''
import pointgenerator
import userapi
import pointgenerator as pg
import meshgenerator


class GearGenerator:
    def __init__(self):
        self.next = 0
        self.spesificationList = [10, 40, 2,  2, 20, 200, 8.3540, 58.2250]
        self.temp = 0
        self.pointsInner = []
        self.p_index = 0
        self._filename = ''

        self.mg = meshgenerator.MeshGenerator()
        self.uApi = userapi.UserApi()
        self.pg = pointgenerator.PointGenerator()

    def inputFase(self):
        '''
        Fase for reciving user input for wanted size of the gear
        '''
        action = self.uApi.userInput()
        if action:
            midleList = self.uApi.getList()
            if midleList[4] != 0:
                self.spesificationList = self.uApi.getList()
            self.next += 1
        return 0

    def meshFase(self):
        '''
        Fase for creating a mesh from the reciving point cloud and save as .stl file
        '''
        action = self.uApi.generatingPMS(self.temp)
        action = True

        #Import Points from point generator
        pointsInner = self.pg.getPointsInner()
        pointsMain = self.pg.getPointsMain()
        pointsOuter =  self.pg.getPointsOuter()
        pointsInnerOffset = self.pg.getPointsInnerOffset()
        pointsMainOffset = self.pg.getPointsMainOffset()
        pointsOuterOffset =  self.pg.getPointsOuterOffset()
        self.mg.inputAndRun(pointsInner, pointsMain, pointsOuter, pointsInnerOffset, pointsMainOffset, pointsOuterOffset, self.spesificationList[1])
        self.mg.faceGenerator()
        self.mg.plotMesh()
        self.mg.generateSTL(self._filename)

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
        action = self.uApi.fetchingTemperature()

        #Rertriving location mean temperature

        if self.p_index == 0:
            # self.uApi.fetchingTemperature()
            # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
            self.pg.inputList(self.spesificationList)
            # Activates all the functions
            self.pg.temperatureSizing()
            self.pg.generatingInnerCircle()
            self.pg.generatingMainCircle()
            self.pg.generatingOuterCircle()
            self.pg.offsetPoints()
            self.temp = self.pg.returnTemp()
            self.p_index = 1

        if action:
            self.next += 1
            self._filename = self.uApi.getFilename()
            print(self._filename)
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
