import sys
import pygame

def main():
    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)

    WIDTH = 1280
    HEIGHT = 800

    x_start, y_start = 0, 0
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

    pygame.display.set_caption("Square")
    font = pygame.font.SysFont("Arial", 18, bold=True)

    def text_display(letter, x_start, y_start):
        text = font.render(str(letter), True, white)
        display_surface.blit(text, (x_start, y_start))

    x, y = 0, 0

    run = True

    while(run):
        screen.fill((black))
        text_display("x:" + str(x) + " y:" + str(y), 0, 0)
        text_display("a", x, y)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= 1
        if keys[pygame.K_DOWN]:
            y += 1
        if keys[pygame.K_LEFT]:
            x -= 1
        if keys[pygame.K_RIGHT]:
            x += 1

        pygame.display.update()

        #closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

def main_old():
    side = 0
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        side = 1
    else:
        side = int(sys.argv[1])
    draw(create_square(side))

def create_square(side):
    square_array = [[0 for j in range(side)] for i in range(side + 1)] 
    #top side
    for i in range(side):
        square_array[0][i] = "_"
    #left and right sides
    for i in range(1, side):
        square_array[i][0] = "|"
        square_array[i][side - 1] = "|"
    #bottom side
    for i in range(side):
        square_array[side][i] = "_"
    return square_array

def draw(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end="")
        print()

if __name__ == "__main__":
    main()