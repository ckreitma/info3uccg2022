import pygame
from functions import is_inside_polygon, pixel, poligon_draw
from math import floor, sin, cos, pi, sqrt
from time import sleep
import numpy

pygame.init()
ancho = 300
alto= 300
canvas = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Gradiente")
lista_puntos = [(190, 167), (145,80), (140, 60),(250, 240) ,(150,240) ,(55, 150)]
exit = False
canvas.fill((0, 0, 0))
p = numpy.array(lista_puntos)
minx, maxx, miny, maxy = p[:, 0].min(), p[:, 0].max(), p[:, 1].min(), p[:, 1].max()
nx = minx + ((maxx-minx)//2)
ny = miny + ((maxy-miny)//2)

centro = {
    'x': nx,
    'y': ny
}

dist_centro_borde = floor(sqrt(pow(nx-maxx,2)+pow(ny-maxy,2)))

r1= dist_centro_borde
r2= dist_centro_borde


while not exit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    
    for j in range(r1):
        r1 = r1 - 1
        r2 = r2 - 1
        for i in range(0, 4575):
            angulo1 = i * (2*pi/ancho)
            angulo2 = i+1 * (2*pi/alto)
            x = centro['x'] + r1*cos(angulo1)
            y = centro['y'] + r2*sin(angulo1)
            if(is_inside_polygon(lista_puntos,(x,y))):
                if(j<255):
                    pygame.draw.aaline(canvas, (0, j, 0), (x, y), (x, y))
                else:
                    pygame.draw.aaline(canvas, (0, 255, 0), (x, y), (x, y))
                pygame.display.update()        
    poligon_draw(canvas,lista_puntos,(255,255,255))


    pygame.display.update()