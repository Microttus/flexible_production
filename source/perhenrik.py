'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
26.10.2022
'''

# TO DO Per Henrik:
# # Correct API to find mean. Not sure about the dates and the mean value
# # Calculate and correct the size of the gear! Think this is OK. The size is returned in prosent. Needs to be printed.
# # Help with the mesh?
# # Update class diagram because API is a function inside PointGeneratic
# # Skriv inn grønn heder i alle funksjonene

import pointgenerator
import meshgenerator

spesificationList = [10, 40, 2,  2, 20, 200, 8.3540, 58.2250]
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

