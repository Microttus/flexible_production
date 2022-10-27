'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
27.10.2022
'''

import numpy as np

class PointGenerator:
    def __init__(self, cirkInner, cirkOuter, teethHeiht, numberOfTeeth):
        self.cirkInner = cirkInner
        self.cirkOuter = cirkOuter
        self.teethHeiht = teethHeiht
        self.numberOfTeeth = numberOfTeeth
        self.cirkMain = cirkOuter - 2*teethHeiht
        self.theta = np.linspace(0, 2*np.pi, self.numberOfTeeth)
        self.thetaShifted = self.theta + self.theta[1]/2



    def generatingInnerCircle(self):

        # make a simple unit circle with teeth number of points
        self.xInner, self.yInner = self.cirkInner/2 * np.cos(self.theta), self.cirkInner/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle


    def generatingMainCircle(self):
         # make a simple unit circle
        self.xMain, self.yMain = self.cirkMain/2 * np.cos(self.theta), self.cirkMain/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle

    def generatingOuterCircle(self):
        # make a simple unit circle shiftet one halv tooth
        self.xOuter, self.yOuter = self.cirkOuter/2 * np.cos(self.thetaShifted), self.cirkOuter/2 * np.sin(self.thetaShifted) #x,y are coordinates for the inner cirkle

    def getDataAndRun(self):
          # [innerDiameter, nuberOfTeeth, printTemperature, teethheight, locationLong, locationLat, locationTemp]
            specificationList = [10, 20, 0, 2, 0, 0, 0]
          #self.generatingInnerCircle(specification[])
    ###
     ##TEST
    ## TEST 3

