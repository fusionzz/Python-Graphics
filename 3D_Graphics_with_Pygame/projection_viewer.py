import wireframe
import pygame
import cube_wireframe

key_to_function = {
        pygame.K_LEFT:   (lambda x: x.translateAll('x', -10)),
        pygame.K_RIGHT:  (lambda x: x.translateAll('x',  10)),
        pygame.K_DOWN:   (lambda x: x.translateAll('y',  10)),
        pygame.K_UP:     (lambda x: x.translateAll('y', -10)),
        pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
        pygame.K_MINUS:  (lambda x: x.scaleAll( 0.8)),
        pygame.K_q: (lambda x: x.rotateAll('X',  0.1)),
        pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
        pygame.K_a: (lambda x: x.rotateAll('Y',  0.1)),
        pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
        pygame.K_z: (lambda x: x.rotateAll('Z',  0.1)),
        pygame.K_x: (lambda x: x.rotateAll('Z', -0.1))
    }

class ProjectionViewer:
    """Displays 3D objects on Pygame screen"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Wireframe Display')
        self.background = self.BLACK

        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColor = self.WHITE
        self.edgeColor = (200, 200, 200)
        self.nodeRadius = 4

    def addWireframe(self, name: str, wireframe: wireframe.Wireframe):
        """Add a named wireframe object"""
        self.wireframes[name] = wireframe

    def translateAll(self, axis:str, d:int):
        for wireframe in self.wireframes.values():
            wireframe.translate(axis, d)

    def scaleAll(self, scale):
        """Scale all wireframes by given scale, centered at center of the screen"""
        center_x = self.width/2
        center_y = self.height/2

        for wireframe in self.wireframes.values():
            wireframe.scale((center_x, center_y), scale)

    def rotateAll(self, axis, theta):
        """Rotate all wireframe about their center along a given axis by theta"""

        rotateFunction = 'rotate' + axis

        for wireframe in self.wireframes.values():
            center = wireframe.findCenter()
            #calls the appropriate rotate function of the wireframe
            getattr(wireframe, rotateFunction)(center, theta)


    def display(self):
        """Draw wireframes on the screen"""

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen, self.edgeColor, (edge.start.x, edge.start.y),
                                     (edge.stop.x, edge.stop.y), 1)
                    
            if self.displayNodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.nodeColor, (node.x, node.y), 
                                       self.nodeRadius, 0)

    def run(self):
        """Create pygame screen until closed"""

        running = True

        while(running):
            #closes window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        key_to_function[event.key](self)
            
            self.display()
            pygame.display.flip()

if __name__ == '__main__':
    my_cube = cube_wireframe.make_cube()

    pv = ProjectionViewer(1280, 800)
    pv.addWireframe('cube', my_cube)
    pv.run()