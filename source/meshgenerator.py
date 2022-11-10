import numpy as np

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
import geargenerator as gg

import pointgenerator as pg
from stl import mesh

class MeshGenerator:
    def __init__(self, pointsInner, pointsMain, pointsOuter , pointsInnerOffset, pointsMainOffset, pointsOuterOffset, D):
        self.pointsInner = pointsInner
        self.pointsMain = pointsMain
        self.pointsOuter = pointsOuter
        self.pointsInnerOffset = pointsInnerOffset
        self.pointsMainOffset = pointsMainOffset
        self.pointsOuterOffset = pointsOuterOffset
        self.D = D #Diameter of the gear
        self.r =self.D/2 #radus of the gear
        self.faceGenerator()
        self.plotMesh()


    def faceGenerator(self):
        self.v = np.vstack((self.pointsInner, self.pointsMain, self.pointsOuter,self.pointsInnerOffset,self.pointsMainOffset, self.pointsOuterOffset))
        self.f = []
        length = len(self.pointsInner)



        for i  in range(1, length):
            var =  np.array([i-1,i,i-1 + length]) # inner lower circle, inn to out triangles
            var2 = np.array([i-1+length,i+length,i]) # mid lower, out to inn triangles. Completes lower inner circle
            var3 = np.array([i-1+length,i+length,i-1+2*length]) # teeth lower
            var4 = np.array([i-1,i,i-1+3*length]) # inner to inner, trangle from lower to higher
            var5 = np.array([i-1+3*length,i+3*length,i]) # inner to inner, trangle from higher to lower
            var6 = np.array([i-1+4*length,i+4*length,i-1+3*length]) # from main to inner top plane
            var7 = np.array([i-1+3*length,i+3*length,i+4*length]) # inner to main top plane
            var8 = np.array([i-1+4*length,i+4*length,i-1+5*length]) # teeth top plane7
            var9 = np.array([i+length,i+4*length,i-1+5*length]) #inner bottom to inner top to teeth
            var10 = np.array([i+length,i+4*length,i+5*length]) #inner bottom to inner top to next teeth
            var11 = np.array([i-1+2*length,i-1+5*length,i+length]) # #teeth bottom and top to inner lower
            var12 = np.array([i-1+2*length,i-1+5*length,i-1+length]) # #teeth bottom and top to inner lower

    #Add to the face list.
            self.f.append(var)
            self.f.append(var2)
            self.f.append(var3)
            self.f.append(var4)
            self.f.append(var5)
            self.f.append(var6)
            self.f.append(var7)
            self.f.append(var8)
            self.f.append(var9)
            self.f.append(var10)
            self.f.append(var11)
            self.f.append(var12)

        self.f = np.vstack(self.f)


    def plotMesh(self):

        fig =plt.figure(figsize=(10,10))
        ax = fig.add_subplot(projection="3d")
        scalex = self.v.shape
        #scaley = scalex/5
        #scalez = scalex/5
        pc = art3d.Poly3DCollection(self.v[self.f],  edgecolor="black")
        ax.add_collection(pc)
        ax.auto_scale_xyz(scalex,scalex,scalex)
        plt.xlim(-self.r,self.r)
        plt.ylim(-self.r, self.r)
        plt.show()



    def printPlot(self):
        """
        Description
        :return:
        Returns the list of the Outer circle with ofset. x = getPointsOuterOffset[0], y = getPointsOuterOffset[1], z = getPointsOuterOffset[2]
        """
        return 0
