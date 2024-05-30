import wireframe
import pygame

class ProjectionViewer:
    """Displays 3D objects on Pygame screen"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, width, height):
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

    def run(self):
        """Create pygame screen until closed"""

        running = True
        while(running):
            #closes window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(self.background)
            pygame.display.flip()