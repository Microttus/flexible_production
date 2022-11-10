import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as scp
from scipy.spatial import Delaunay


class nodes:
    def __init__(self):
        self.nodes = []
        self.numberOfElements = 0
        self.lengthIncrement = 0.2
        self.heightIncrement = 0.3
        self.points = []
        self.tri = []

    def setNbElements(self,numberOfElements):
        self.numberOfElements = numberOfElements

    def arrayGenerator(self):
        for x in np.linspace(0, self.lengthIncrement, num=self.numberOfElements):
            for y in np.linspace(0, self.heightIncrement, num=self.numberOfElements):
                self.nodes.append([x, y])

        self.points = np.array(self.nodes)


    def ploting(self):
        self.tri = Delaunay(self.points)
        plt.triplot(self.points[:,0], self.points[:,1], self.tri.simplices)
        plt.plot(self.points[:, 0], self.points[:, 1], 'o')
        print(self.points[:,0])
        plt.show()


class PointGenerator:
    def __init__(self): #, cirkInner, cirkOuter, teethHeiht, numberOfTeeth
        self.cirkInner = 0 #cirkInner
        self.cirkOuter = 0 #cirkOuter
        self.teethHeiht = 0 #teethHeiht
        self.numberOfTeeth = 0 #numberOfTeeth
        self.cirkMain = 0 #cirkOuter - 2*teethHeiht
        self.theta = 0 #np.linspace(0, 2*np.pi, self.numberOfTeeth)
        self.thetaShifted = 0 #self.theta + self.theta[1]/2
        self.outerpoints = []
        self.outerNodes = []
        self.mainPoints = []
        self.mainNodes = []
        self.innerPoints = []
        self.innerNodes = []
        self.triA = []  # not sure what tri is
        self.triB = []
        self.test = []
    def giveValues(self,cirkInner, cirkOuter, teethHeiht, numberOfTeeth):
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
        self.innerNodes = list(zip(self.xInner, self.yInner))
        self.innerPoints = np.array(self.innerNodes)


    def generatingMainCircle(self):
         # make a simple unit circle
        self.xMain, self.yMain = self.cirkMain/2 * np.cos(self.theta), self.cirkMain/2 * np.sin(self.theta) #x,y are coordinates for the inner cirkle
        self.mainNodes = list(zip(self.xMain, self.yMain))
        self.mainPoints = np.array(self.mainNodes)

    def generatingOuterCircle(self):
        # make a simple unit circle shiftet one halv tooth
        self.xOuter, self.yOuter = self.cirkOuter/2 * np.cos(self.thetaShifted), self.cirkOuter/2 * np.sin(self.thetaShifted) #x,y are coordinates for the inner cirkle
        self.outerNodes = list(zip(self.xOuter, self.yOuter))
        self.outerpoints = np.array(self.outerNodes)


        self.test = list(zip(self.outerpoints,self.mainPoints))
        self.test = np.array(self.test)
        #self.triA = Delaunay(self.test)

        print(self.test)
       # plt.triplot(self.test[:, 0], self.test[:, 1], self.triA.simplices)
        #plt.plot(self.points[:, 0], self.points[:, 1], 'o')
        #plt.show()





