'''
Gear Generator MAS417 Project
Flexible Production
Per Henrik Hardeberg
26.10.2022
'''

import pointgenerator as pg
import numpy as np
import matplotlib.pyplot as plt


ring = pg.PointGenerator(10,20,2, 20)
ring.generatingInnerCircle() #Run the function just to get the points. To be moved for automatically run
ring.generatingMainCircle()
ring.generatingOuterCircle()

plt.plot(ring.xInner, ring.yInner, '*')
plt.plot(ring.xMain, ring.yMain, '*')
plt.plot(ring.xOuter, ring.yOuter, '*')
plt.show()
