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
## Løse for null


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
import pointgenerator as pg
from stl import mesh


dummyList = [0.1, 0.5, 0.05,  0.05,25, 200,8.3540, 58.2250]
        # [innerDiameter, outerDiameter, teethheight,gearheight, nuberOfTeeth, printTemperature [C],  locationLat, locationLong]
pGen = pg.PointGenerator(dummyList) #Her oprettes objektet, bytt til spesification list når den skal testes skikkelig.
pointsInner = pGen.getPointsInner()
pointsMain = pGen.getPointsMain()
pointsOuter =  pGen.getPointsOuter()
pointsInnerOffset = pGen.getPointsInnerOffset()
pointsMainOffset = pGen.getPointsMainOffset()
pointsOuterOffset =  pGen.getPointsOuterOffset()

#v = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0],
   #          [0,0,1], [1,0,1], [1,1,1], [0,1,1]])

#f = np.array([[0,6,1]])



v = np.vstack((pointsInner, pointsMain, pointsOuter,pointsInnerOffset,pointsMainOffset, pointsOuterOffset))
f = []
length = len(pointsInner)
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
    f.append(var)
    f.append(var2)
    f.append(var3)
    f.append(var4)
    f.append(var5)
    f.append(var6)
    f.append(var7)
    f.append(var8)
    f.append(var9)
    f.append(var10)
    f.append(var11)
    f.append(var12)


f = np.vstack(f)   # To get the faces to mach the array expected and not array of array
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
pc = art3d.Poly3DCollection(v[f],  edgecolor="black")
ax.add_collection(pc)
plt.show()




gear = mesh.Mesh(np.zeros(f.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(f):
    for j in range(3):
        gear.vectors[i][j] = v[f[j],:]

print(enumerate(f))

 #Write the mesh to file "cube.stl"
gear.save('gearPrint.stl')
print(len(gear.vectors))



''' 
  #Plot the points just for fun
        ax = plt.axes(projection='3d')
        plt.plot(pointsInner[:, 0],pointsInner[:,1],pointsInner[:,2], '*')
        plt.plot(pointsMain[:,0], pointsMain[:,1], pointsMain[:,2], '*')
        plt.plot(pointsOuter[:,0], pointsOuter[:,1], pointsOuter[:,2], '*')

        plt.plot(pointsInnerOffset[:, 0],pointsInnerOffset[:,1],pointsInnerOffset[:,2], '*')
        plt.plot(pointsMainOffset[:, 0], pointsMainOffset[:,1], pointsMainOffset[:,2], '*')
        plt.plot(pointsOuterOffset[:, 0], pointsOuterOffset[:,1], pointsOuterOffset[:,2], '*')
        plt.show()

        # Sett inn meshing her
        # Torbjørn
        #

'''
