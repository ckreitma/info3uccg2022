# https://codeloop.org/python-opengl-programming-drawing-teapot/
from OpenGL.GLUT import *
from OpenGL.GL import *


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)  # Apunta a la matriz de proyección
    glLoadIdentity()
    # Matriz de proyección ortogonal
    # Matriz de proyección ortogonal
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glRotatef(0, 0.1, 0.1, 0.1)
    glutWireTeapot(0.4)
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow("My Second OpenGL Program")
glutDisplayFunc(draw)
glutMainLoop()
