from wireframe import *

def make_cube():
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    print(cube_nodes)
    cube = Wireframe()
    cube.addNodes(cube_nodes)
    print(cube.printNodes())

if __name__ == "__main__":
    make_cube()