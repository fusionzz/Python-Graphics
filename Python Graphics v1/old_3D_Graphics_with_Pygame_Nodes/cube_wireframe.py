import wireframe

def make_cube() -> wireframe.Wireframe:
    cube_nodes = [wireframe.Node([x,y,z]) for x in (50,250) for y in (50,250) for z in (50,250)]
    #edges of cube with node indeces
    cube_edges = [[0,1],[0,2],[0,4],[5,1],[5,4],[5,7],[1,3],[4,6],[2,6],[2,3],[7,3],[7,6]]
    cube = wireframe.Wireframe()
    cube.addNodes(cube_nodes)
    cube.addEdges(cube_edges)
    return cube

if __name__ == "__main__":
    make_cube()