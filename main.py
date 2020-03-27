
import pygame
import file_importer as fi
from math import pi

pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('3D OBJ File Renderer')
clock, fps = pygame.time.Clock(), 30

screen_plane = (300, 300)

path = 'TestModels/robot.obj'
shape = fi.load_obj(path, screen_plane, size)
shape.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    screen.fill(0)

    shape.rotate()
    shape.draw_face(screen)

    pygame.display.update()
    clock.tick(fps)
