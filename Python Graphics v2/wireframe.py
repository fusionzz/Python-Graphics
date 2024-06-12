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
        # self.matrix = np.array({
        #     [self.x, 0, 0, 1],
        #     [0, self.y, 0, 1],
        #     [0, 0, self.z, 1],
        #     [0, 0, 0, 1]
        # })
        # self.vector = np.array([self.x, self.y, self.z])

    def __str__(self) -> str:
        return f"x:{self.x} y:{self.y} z:{self.z}"

# """
# Triangle made up of vertices
# Can add functions to preprcess some rasterization maybe
# """
# class Triangle:
#     def __init__(self, vertex_1 = Vertex(x=0,y=0,z=0), vertex_2 = Vertex(x=0,y=0,z=0), vertex_3 = Vertex(x=0,y=0,z=0)) -> None:
#         self.vertices = [vertex_1, vertex_2, vertex_3]

#     def __str__(self) -> str:
#         tri_string = ""
#         for i in range(3):
#             tri_string += f"Vertex {i+1}: {str(self.vertices[i])}\t"
#         return tri_string

"""
Wireframe class made up of triangles
"""
class Wireframe:
    def __init__(self) -> None:
        self.vertices = []
        self.triangles = []

    def __str__(self) -> str:
        wf_str = ""
        for i in range(len(self.triangles)):
            wf_str += f"""Triangle {i+1}:\n\tVertex 1: {self.vertices[self.triangles[i][0]]}\n
                                            \tVertex 2: {self.vertices[self.triangles[i][1]]}\n
                                            \tVertex 3: {self.vertices[self.triangles[i][2]]}\n"""
        return wf_str
    
    """
    Creates wireframe from obj file
    """
    def fromObj(self, obj_file: str) -> None:
        f = open(obj_file, "r")
        for line in f:
            line = line.split(" ")
            if line[0] == "v":
                vertex = Vertex(x = line[1], y = line[2], z = line[3])
                self.vertices.append(vertex)
            elif line[0] == "f":
                self.triangles.append([int(line[1]) - 1, int(line[2]) - 1, int(line[3]) - 1])
        f.close()

wf = Wireframe()
wf.fromObj("VideoShip.obj")
print(wf)