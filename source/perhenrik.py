'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
26.10.2022
'''

import pointgenerator as pg
import matplotlib.pyplot as plt

specificationList = [5, 20, 3,  3,20, 200,8.3540, 58.2250]
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
ring = pg.PointGenerator(specificationList)


ax = plt.axes(projection='3d')
plt.plot(ring.pointsInner[0],ring.pointsInner[1],ring.pointsInner[2], '*')
plt.plot(ring.xMain, ring.yMain, ring.zMain, '*')
plt.plot(ring.xOuter, ring.yOuter, ring.zOuter, '*')

plt.plot(ring.xInnerOffset, ring.yInnerOffset, ring.zInnerOffset, '*')
plt.plot(ring.xMainOffset, ring.yMainOffset, ring.zMainOffset, '*')
plt.plot(ring.xOuterOffset, ring.yOuterOffset, ring.zOuterOffset, '*')
plt.show()

print(ring.meanTemp)


# TO DO: Correct API to find mean. Not sure about the dates and the mean value
# # Calculate and correct the size of the gear!
# # Point generator to speak with api and run from there
# # Return points to lists??
# # Help with the mesh?

