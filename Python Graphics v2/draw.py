from wireframe import Wireframe
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_W = 1280
SCREEN_H = 800

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Display")
    running = True
    clock = pygame.time.Clock()
    surface = pygame.surface.Surface((SCREEN_W, SCREEN_H))

    wf = Wireframe()
    wf.fromObj("VideoShip.obj")

    while (running):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        screen.fill(BLACK)
        #pygame.draw.line(screen, WHITE, (-100.2,-100.2), (200, 200))
        display(wf, screen)
        pygame.display.flip()

def display(wireframe: Wireframe, screen) -> None:
    for triangle in wireframe.triangles:
        pygame.draw.aaline(screen, WHITE, 
            (wireframe.vertices[triangle[0]].x, wireframe.vertices[triangle[0]].y), (wireframe.vertices[triangle[1]].x, wireframe.vertices[triangle[1]].y))

        pygame.draw.aaline(screen, WHITE, 
            (wireframe.vertices[triangle[1]].x, wireframe.vertices[triangle[1]].y), (wireframe.vertices[triangle[2]].x, wireframe.vertices[triangle[2]].y))

        pygame.draw.aaline(screen, WHITE, 
            (wireframe.vertices[triangle[0]].x, wireframe.vertices[triangle[0]].y), (wireframe.vertices[triangle[2]].x, wireframe.vertices[triangle[2]].y))



if __name__ == '__main__':
    main()