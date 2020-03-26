
import pygame
import file_importer as fi

pygame.init()
size = (1000, 700)
screen = pygame.display.set_mode(size)
clock, fps = pygame.time.Clock(), 30

bounding_box = 100

path = 'models/cube.obj'
shape = fi.load_obj(path, size, bounding_box)
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

    shape.rotate(0, 0.01, 0)
    shape.draw_face(screen, size)

    pygame.display.update()
    clock.tick(fps)
