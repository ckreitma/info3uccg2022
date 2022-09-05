import pygame

# Ancho y alto teórico
ancho_teorico = 500
alto_teorico = 500

# Ancho y alto real
ancho_real = 100
alto_real = 100

# Relation (ratio) de aspecto entre el real y el teórico
delta_x = int(ancho_teorico/ancho_real)
delta_y = int(alto_teorico/alto_real)

screen = pygame.display.set_mode((ancho_teorico, alto_teorico))
running = True

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRIS = (80, 80, 80)
ROJO = (255, 10, 10)


def dibujar_grilla(screen):

    # Lineas horizontales
    for pos_y in range(0, alto_teorico, delta_y):
        # print(f'pos_y={pos_y}')
        pygame.draw.aaline(screen, GRIS, (0, pos_y), (ancho_teorico, pos_y))

    # Lineas verticales
    for pos_x in range(0, ancho_teorico, delta_x):
        # print(f'pos_y={pos_y}')
        pygame.draw.aaline(screen, GRIS, (pos_x, 0), (pos_x, alto_teorico))


def pixel(screen, x, y, color):
    x = int(x)
    y = int(y)
    if x < 0 or x > ancho_real or y < 0 or y > alto_real:
        print(f'Punto incorrecto <{x},{y}>')
        return
    pixel_real = (x*delta_x, (alto_real-y)*delta_y, delta_x, delta_y)
    print(f'Pixel real={pixel_real}')
    # Rectángulo (<origen>,<ancho>,<alto>)
    pygame.draw.rect(screen, color, pixel_real)


def transformar(punto, factorx=1, factory=1):
    return (punto[0]*factorx, punto[1]*factory)


def linea_dda(screen, x0, y0, x1, y1, color):
    pendiente = (y1-y0)/(x1-x0)
    print(f'Pendiente={pendiente}')
    if pendiente < 1.0:
        y = y0*1.0
        for x in range(round(x0), round(x1)):
            pixel(screen, round(x), round(y), color)
            y = y + pendiente
    if pendiente >= 1:  # La y se mueve más rápido que la x
        pendiente = (x1-x0)/(y1-y0)
        x = x0*1.0
        for y in range(round(y0), round(y1)):
            pixel(screen, round(x), round(y), color)
            x = x + pendiente

    # Linea real
    # Se calculan los puntos reales.abs
    punto0_real = (x0*delta_x+delta_x/2.0, (alto_real-y0)*delta_y+delta_y/2.0)    
    punto1_real = (x1*delta_x+delta_x/2.0, (alto_real-y1)*delta_y+delta_y/2.0)    
    pygame.draw.aaline(screen,ROJO,punto0_real,punto1_real)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    screen.fill(BLACK)
    # pygame.draw.rect(screen, BLUE, (200, 150, 100, 50))
    # pygame.draw.aaline(screen, (0, 100, 255), (0, 0), (ancho-1, alto-1))
    # pygame.draw.aaline(screen, (50, 180, 40), (ancho-1, 0), (0, alto-1))
    dibujar_grilla(screen)
    punto1 = (4, 17)
    pixel(screen, punto1[0], punto1[1], WHITE)
    punto2 = (45.3, 80.1)
    pixel(screen, punto2[0], punto2[1], WHITE)
    #transformado = transformar(punto, 1.3, 2.4)
    #pixel(screen, transformado[0], transformado[1], ROJO)
    linea_dda(screen, punto1[0], punto1[1], punto2[0], punto2[1], GRIS)
    #linea(screen, 12, 20, 50, 25, GRIS)
    pygame.display.flip()