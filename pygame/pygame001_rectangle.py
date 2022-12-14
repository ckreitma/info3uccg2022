# https://www.geeksforgeeks.org/getting-started-with-pygame/
import pygame

pygame.init()

color = (255, 255, 255)
rect_color = (255, 0, 0)

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
pygame.display.set_caption("UCCG PyGame 001")

exit = False

while not exit:
    canvas.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.draw.rect(canvas, rect_color, pygame.Rect(30, 30, 60, 60))

    # NO APAREZCA ASI EL lunes
    #pygame.draw.aaline(canvas, (200, 200, 255), (10, 60), (200, 100))
    pygame.display.update()
