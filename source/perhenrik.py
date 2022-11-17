'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
26.10.2022
'''

# TO DO Per Henrik:
# # Update class diagram because API is a function inside PointGeneratic
# # Skriv inn grønn heder i alle funksjonene

import pointgenerator
import meshgenerator
import matplotlib.pyplot as plt
import numpy as np


spesificationList = [20, 60, 5, 10, 15, 210, 8.3540, 58.2250]
pg = pointgenerator.PointGenerator()
mg = meshgenerator.MeshGenerator()
pg.inputList(spesificationList)
pg.temperatureSizing()

pg.generatingInnerCircle()
pg.generatingMainCircle()
pg.generatingOuterCircle()
pg.offsetPoints()
temp = pg.returnTemp()


pointsInner = pg.getPointsInner()
pointsMain = pg.getPointsMain()
pointsOuter =  pg.getPointsOuter()
pointsInnerOffset = pg.getPointsInnerOffset()
pointsMainOffset = pg.getPointsMainOffset()
pointsOuterOffset =  pg.getPointsOuterOffset()

mg.inputAndRun(pointsInner, pointsMain, pointsOuter, pointsInnerOffset, pointsMainOffset, pointsOuterOffset, spesificationList[1])
mg.faceGenerator()
mg.plotMesh()




ax = plt.axes(projection='3d')
plt.plot(pointsInner[:, 0],pointsInner[:,1],pointsInner[:,2], '*')
plt.plot(pointsMain[:,0], pointsMain[:,1], pointsMain[:,2], '*')
plt.plot(pointsOuter[:,0], pointsOuter[:,1], pointsOuter[:,2], '*')

plt.plot(pointsInnerOffset[:, 0],pointsInnerOffset[:,1],pointsInnerOffset[:,2], '*')
plt.plot(pointsMainOffset[:, 0], pointsMainOffset[:,1], pointsMainOffset[:,2], '*')
plt.plot(pointsOuterOffset[:, 0], pointsOuterOffset[:,1], pointsOuterOffset[:,2], '*')
plt.show()

