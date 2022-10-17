# Test for class

import numpy as np
from stl import mesh

a = 0
b = -5

# Define the 8 vertices of the cube
vertices = np.array([\
    [3,0,0],
    [4,1,0],
    [2,1,0],
    [3,2,0],
    [6,1,0],
    [0,1,0],
    [1,2,0],
    [6,2,0],
    [6,3,0],
    [4,3,0],
    [2,3,0],
    [0,3,0],
    [3,4,0],
])
# Define the 12 triangles composing the cube
c = 0

faces = np.array([\
    [0, 1, 2],
    [1, 2, 3],
    [2, 3, 6],
    [2, 5, 6],
    [1, 3, 7],
    [1, 4, 7],
    [3, 7, 9],
    [7, 8, 8],
    [3, 9, 10],
    [3, 6, 10],
    [6, 10, 11],
    [9, 10, 12],
])

#faces2 = np.array([\
 #   [0 1 ]])
# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]

print(enumerate(faces))

# Write the mesh to file "cube.stl"
cube.save('cube.stl')
print(len(cube.vectors))