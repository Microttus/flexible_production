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


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
import pointgenerator as pg
dummyList = [0.2, 0.5, 0.1,  0.1,20, 200,8.3540, 58.2250]
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
pGen = pg.PointGenerator(dummyList) #Her oprettes objektet, bytt til spesification list når den skal testes skikkelig.
pointsInner = pGen.getPointsInner()
pointsMain = pGen.getPointsMain()
pointsOuter =  pGen.getPointsOuter()
pointsInnerOffset = pGen.getPointsInnerOffset()
pointsMainOffset = pGen.getPointsMainOffset()
pointsOuterOffset =  pGen.getPointsOuterOffset()

#v = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0],
 #             [0,0,1], [1,0,1], [1,1,1], [0,1,1]])

#v = np.array([pointsInner, pointsMain])

#f = np.array([[0,6,1], [1,2,3]])

v = np.vstack((pointsInner, pointsMain, pointsOuter))
f = []
for i  in range(1, len(pointsInner)):
    var =  np.array([i-1,i,i-1 + len(pointsInner)])
    var2 = np.array([i-1+len(pointsInner),i+len(pointsInner),i])
    var3 = np.array([i-1+len(pointsInner),i+len(pointsInner),i-1+2*len(pointsInner)])
    f.append(var)
    f.append(var2)
    f.append(var3)



fig = plt.figure()
ax = fig.add_subplot(projection="3d")
pc = art3d.Poly3DCollection(v[f],  edgecolor="black")
ax.add_collection(pc)
plt.show()
