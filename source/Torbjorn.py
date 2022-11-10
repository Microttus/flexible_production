import matplotlib.pyplot as plt
import numpy as np

import meshgenerator

nd = klassertorbjorn.nodes()
pg = klassertorbjorn.PointGenerator()


#---Main flow---
def main():
    plotnodes()
#    meshgears()
#---Functions---
def plotnodes():
    nd.setNbElements(20)
    nd.arrayGenerator()
    nd.ploting()

def meshgears():
    pg.giveValues(10,20,2,20)
    pg.generatingInnerCircle()#Run the function just to get the points. To be moved for automatically run
    pg.generatingMainCircle()
    pg.generatingOuterCircle()

#    plt.plot(pg.xInner, pg.yInner, '*')
#    plt.plot(pg.xMain, pg.yMain, '*')
#    plt.plot(pg.xOuter, pg.yOuter, '*')
#    plt.show()




# Running main
main()


