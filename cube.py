import sys
import pygame
import math

def main():
    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)

    WIDTH = 1280
    HEIGHT = 800

    x_seperator = 10
    y_seperator = 20

    rows = HEIGHT // y_seperator
    columns = WIDTH // x_seperator
    screen_size = rows * columns

    x_offset = columns / 2
    y_offset = rows / 2

    

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #choose between resolution or fullscreen
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    #display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("Cube")
    font = pygame.font.SysFont("Arial", 18, bold=True)

    #puts text on screen at position
    def text_display(letter, x_start, y_start):
        text = font.render(str(letter), True, white)
        display_surface.blit(text, (x_start, y_start))

    #coords of cube in hypothetical 3d plane
    # point c is at starting coords
    #side length is variable "side"
    #
    #      a-----b
    #      |  e----f  
    #      |  |    |
    #      c--|--d |
    #         g----h

    #distance to camera
    distance_to_camera = 1000

    side = 100
    x_start, y_start, z_start = WIDTH / 2, HEIGHT / 2, 100

    c = (x_start, y_start, z_start)
    d = (x_start + side, y_start, z_start)
    a = (x_start, y_start + side, z_start)
    b = (x_start + side, y_start + side, z_start)
    e = (x_start, y_start + side, z_start + side)
    f = (x_start + side, y_start + side, z_start + side)
    g = (x_start, y_start, z_start + side)
    h = (x_start + side, y_start, z_start + side)

    #convert to 2d coords version1
    def perspective_projection(old_coords, camera_distance):
        x = old_coords[0]
        y = old_coords[1]
        z = old_coords[2]

        new_x = (camera_distance/(camera_distance + z)) * x
        new_y = (camera_distance/(camera_distance + z)) * y

        return (new_x, new_y)
    
    #version2
    #f = focal lengths, c = coords of principal point
    #basically c means coords of plane?
    #not sure what f means
    def to_3d(old_coords, f_x, f_y, c_x, c_y):
        x = old_coords[0]
        y = old_coords[1]
        z = old_coords[2]

        new_x = (x / z) * f_x + c_x
        new_y = (y / z) * f_y + c_y

        return (new_x, new_y)
    
    new_a = perspective_projection(a, distance_to_camera)
    new_b = perspective_projection(b, distance_to_camera)
    new_c = perspective_projection(c, distance_to_camera)
    new_d = perspective_projection(d, distance_to_camera)
    new_e = perspective_projection(e, distance_to_camera)
    new_f = perspective_projection(f, distance_to_camera)
    new_g = perspective_projection(g, distance_to_camera)
    new_h = perspective_projection(h, distance_to_camera)

    f_x, f_y, c_x, c_y = 10,10,10,10
    newnew_a = to_3d(a, f_x, f_y, c_x, c_y)
    newnew_b = to_3d(b, f_x, f_y, c_x, c_y)
    newnew_c = to_3d(c, f_x, f_y, c_x, c_y)
    newnew_d = to_3d(d, f_x, f_y, c_x, c_y)
    newnew_e = to_3d(e, f_x, f_y, c_x, c_y)
    newnew_f = to_3d(f, f_x, f_y, c_x, c_y)
    newnew_g = to_3d(g, f_x, f_y, c_x, c_y)
    newnew_h = to_3d(h, f_x, f_y, c_x, c_y)


    run = True

    while(run):
        screen.fill((black))

        #displays x and y coords
        #text_display("x:" + str(x) + " y:" + str(y), 0, 0)

        #text_display("Distance to camera: " + str(distance_to_camera), 0, 0)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     distance_to_camera -= 1
        #     if distance_to_camera <= 0:
        #         distance_to_camera = 1
        # if keys[pygame.K_DOWN]:
        #     distance_to_camera += 1
        # if keys[pygame.K_LEFT]:
        #     x -= 1
        # if keys[pygame.K_RIGHT]:
        #     x += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            f_y -= 1
        if keys[pygame.K_DOWN]:
            f_y += 1
        if keys[pygame.K_LEFT]:
            f_x -= 1
        if keys[pygame.K_RIGHT]:
            f_x += 1
        if keys[pygame.K_w]:
            c_y -= 1
        if keys[pygame.K_s]:
            c_y += 1
        if keys[pygame.K_d]:
            c_x -= 1
        if keys[pygame.K_a]:
            c_x += 1


        new_a = perspective_projection(a, distance_to_camera)
        new_b = perspective_projection(b, distance_to_camera)
        new_c = perspective_projection(c, distance_to_camera)
        new_d = perspective_projection(d, distance_to_camera)
        new_e = perspective_projection(e, distance_to_camera)
        new_f = perspective_projection(f, distance_to_camera)
        new_g = perspective_projection(g, distance_to_camera)
        new_h = perspective_projection(h, distance_to_camera)

        newnew_a = to_3d(a, f_x, f_y, c_x, c_y)
        newnew_b = to_3d(b, f_x, f_y, c_x, c_y)
        newnew_c = to_3d(c, f_x, f_y, c_x, c_y)
        newnew_d = to_3d(d, f_x, f_y, c_x, c_y)
        newnew_e = to_3d(e, f_x, f_y, c_x, c_y)
        newnew_f = to_3d(f, f_x, f_y, c_x, c_y)
        newnew_g = to_3d(g, f_x, f_y, c_x, c_y)
        newnew_h = to_3d(h, f_x, f_y, c_x, c_y)

        #version1 3d
        # pygame.draw.line(screen, white, new_a, new_b)
        # pygame.draw.line(screen, white, new_a, new_c)
        # pygame.draw.line(screen, white, new_a, new_e)
        # pygame.draw.line(screen, white, new_b, new_d)
        # pygame.draw.line(screen, white, new_b, new_f)
        # pygame.draw.line(screen, white, new_c, new_d)
        # pygame.draw.line(screen, white, new_c, new_g)
        # pygame.draw.line(screen, white, new_d, new_h)
        # pygame.draw.line(screen, white, new_e, new_f)
        # pygame.draw.line(screen, white, new_e, new_g)
        # pygame.draw.line(screen, white, new_f, new_h)
        # pygame.draw.line(screen, white, new_g, new_h)

        #version2 3d
        pygame.draw.line(screen, white, newnew_a, newnew_b)
        pygame.draw.line(screen, white, newnew_a, newnew_c)
        pygame.draw.line(screen, white, newnew_a, newnew_e)
        pygame.draw.line(screen, white, newnew_b, newnew_d)
        pygame.draw.line(screen, white, newnew_b, newnew_f)
        pygame.draw.line(screen, white, newnew_c, newnew_d)
        pygame.draw.line(screen, white, newnew_c, newnew_g)
        pygame.draw.line(screen, white, newnew_d, newnew_h)
        pygame.draw.line(screen, white, newnew_e, newnew_f)
        pygame.draw.line(screen, white, newnew_e, newnew_g)
        pygame.draw.line(screen, white, newnew_f, newnew_h)
        pygame.draw.line(screen, white, newnew_g, newnew_h)

        pygame.display.update()

        #closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    main()