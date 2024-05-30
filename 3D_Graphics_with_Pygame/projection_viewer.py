import wireframe
import pygame
import cube_wireframe

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

    def transformAll(self, axis:str, d:int):
        for wireframe in self.wireframes.values():
            wireframe.translate(axis, d)

    def scaleAll(self, scale):
        pass


    def display(self):
        """Draw wireframes on the screen"""

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.line(self.screen, self.edgeColor, (edge.start.x, edge.start.y),
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
            
            self.display()
            pygame.display.flip()

if __name__ == '__main__':
    my_cube = cube_wireframe.make_cube()

    pv = ProjectionViewer(1280, 800)
    pv.addWireframe('cube', my_cube)
    pv.run()