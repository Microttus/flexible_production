import matplotlib.pyplot as plt
import numpy as np

import klassertorbjorn
import pointgenerator as pp
import scipy as scp
from scipy.spatial import Delaunay
nd = klassertorbjorn.nodes()
pg = klassertorbjorn.PointGenerator()


# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np
import pointgenerator as pp
#example----- start----
# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 24
n_radii = 9
min_radius = 0.5
radii = np.linspace(min_radius, 0.9,
					n_radii)

angles = np.linspace(0, 3 * np.pi, n_angles,
					endpoint = False)

angles = np.repeat(angles[..., np.newaxis],
				n_radii, axis = 1)

angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis = 1),
						y[triang.triangles].mean(axis = 1))
				< min_radius)

plt.triplot(triang, 'go-', lw = 1)
plt.title('matplotlib.pyplot.triplot() Example')
plt.show()

#----Example end---------------









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
#main()


