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

spesificationList = [15, 60, 5, 10, 25, 210, 8.3540, 58.2250]
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

