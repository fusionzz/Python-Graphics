import pygame

def main():
    pygame.init()

    WIDTH = 1280
    HEIGHT = 800

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #choose between resolution or fullscreen
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    #display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("Cube")

    white = (255, 255, 255)
    black = (0, 0, 0)

     #coords of cube in hypothetical 3d plane
    # point c is at starting coords
    #side length is variable "side"
    #
    #      a-----b
    #      |  e----f  
    #      |  |    |
    #      c--|--d |
    #         g----h

    x_start, y_start, z_start = WIDTH / 2, HEIGHT / 2, 100
    side_length = 100

    c = [x_start, y_start, z_start]
    d = [x_start + side_length, y_start, z_start]
    a = [x_start, y_start + side_length, z_start]
    b = [x_start + side_length, y_start + side_length, z_start]
    e = [x_start, y_start + side_length, z_start + side_length]
    f = [x_start + side_length, y_start + side_length, z_start + side_length]
    g = [x_start, y_start, z_start + side_length]
    h = [x_start + side_length, y_start, z_start + side_length]

    def wiki3d(point_coords, camera_coords, screen_coords):
        a_x = point_coords[0]
        a_y = point_coords[1]
        a_z = point_coords[2]

        c_x = camera_coords[0]
        c_y = camera_coords[1]
        c_z = camera_coords[2]

        e_x = screen_coords[0]
        e_y = screen_coords[1]
        e_z = screen_coords[2]

        d_x = a_x - c_x
        d_y = a_y - c_y
        d_z = a_z - c_z

        b_x = (e_z/d_z) * d_x + e_x
        b_y = (e_z/d_z) * d_y + e_y

        return (b_x, b_y)
    
    camera_coords = [0,0,0]
    screen_coords = [0,0,200]

    run = True

    while(run):
        screen.fill((black))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            camera_coords[1] += 1
        if keys[pygame.K_s]:
            camera_coords[1] -= 1
        if keys[pygame.K_a]:
            camera_coords[0] -= 1
        if keys[pygame.K_d]:
            camera_coords[0] += 1
        if keys[pygame.K_UP]:
            screen_coords[1] += 1
        if keys[pygame.K_DOWN]:
            screen_coords[1] -= 1
        if keys[pygame.K_LEFT]:
            screen_coords[0] -= 1
        if keys[pygame.K_RIGHT]:
            screen_coords[0] += 1

        new_a = wiki3d(a, camera_coords, screen_coords)
        new_b = wiki3d(b, camera_coords, screen_coords)
        new_c = wiki3d(c, camera_coords, screen_coords)
        new_d = wiki3d(d, camera_coords, screen_coords)
        new_e = wiki3d(e, camera_coords, screen_coords)
        new_f = wiki3d(f, camera_coords, screen_coords)
        new_g = wiki3d(g, camera_coords, screen_coords)
        new_h = wiki3d(h, camera_coords, screen_coords)

        pygame.draw.line(screen, white, new_a, new_b)
        pygame.draw.line(screen, white, new_a, new_c)
        pygame.draw.line(screen, white, new_a, new_e)
        pygame.draw.line(screen, white, new_b, new_d)
        pygame.draw.line(screen, white, new_b, new_f)
        pygame.draw.line(screen, white, new_c, new_d)
        pygame.draw.line(screen, white, new_c, new_g)
        pygame.draw.line(screen, white, new_d, new_h)
        pygame.draw.line(screen, white, new_e, new_f)
        pygame.draw.line(screen, white, new_e, new_g)
        pygame.draw.line(screen, white, new_f, new_h)
        pygame.draw.line(screen, white, new_g, new_h)

        pygame.display.update()

        #closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    main()

        



