
import pygame
import file_importer as fi
from math import pi

pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('3D OBJ File Renderer')
clock, fps = pygame.time.Clock(), 30

screen_plane = (300, 300)

path = 'D:/Blender/Projects/textured cube/Exported/textured cube.obj'
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

    shape.rotate(x=0.01, y=0.01)
    shape.draw_line(screen)
    # shape.draw_face(screen)

    screen.blit(shape.texture, (0, 0))
    for vert in shape.texture_verts:
        pygame.draw.circle(screen, [150, 0, 0], vert.get_xy(), 2)


    pygame.display.update()
    clock.tick(fps)
