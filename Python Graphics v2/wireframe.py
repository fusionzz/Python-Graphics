"""
Wireframe class which can take in an obj file (or manually create)
a wireframe made out of triangles
"""

import numpy as np

"""
Vertex class which has matrix and vector forms
"""
class Vertex:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.matrix = np.array({
            [self.x, 0, 0, 1],
            [0, self.y, 0, 1],
            [0, 0, self.z, 1],
            [0, 0, 0, 1]
        })
        self.vector = np.array([self.x, self.y, self.z])

    def __str__(self) -> str:
        return f"x:{self.x} y:{self.y} z:{self.z}\n"

"""
Triangle made up of vertices
Can add functions to preprcess some rasterization maybe
"""
class Triangle:
    def __init__(self, vertex_1 = Vertex(x=0,y=0,z=0), vertex_2 = Vertex(x=0,y=0,z=0), vertex_3 = Vertex(x=0,y=0,z=0)) -> None:
        self.vertices = [vertex_1, vertex_2, vertex_3]

    def __str__(self) -> str:
        tri_string = ""
        for i in range(3):
            tri_string += f"Vertex {i+1}: {str(self.vertices[i])}"
        return tri_string
