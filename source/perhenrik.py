'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
26.10.2022
'''

import pointgenerator as pg
import numpy as np
import matplotlib.pyplot as plt

specificationList = [5, 20, 3, 20, 3, 200,8.3540, 58.2250]
        # [innerDiameter, outerDiameter, thickness, nuberOfTeeth,teethheight, printTemperature [C],  locationLat, locationLong]
ring = pg.PointGenerator(specificationList)


ax = plt.axes(projection='3d')
plt.plot(ring.xInner, ring.yInner, ring.zInner, '*')
plt.plot(ring.xMain, ring.yMain, ring.zMain, '*')
plt.plot(ring.xOuter, ring.yOuter, ring.zOuter, '*')

plt.plot(ring.xInnerOffset, ring.yInnerOffset, ring.zInnerOffset, '*')
plt.plot(ring.xMainOffset, ring.yMainOffset, ring.zMainOffset, '*')
plt.plot(ring.xOuterOffset, ring.yOuterOffset, ring.zOuterOffset, '*')
plt.show()

print(ring.meanTemp)

