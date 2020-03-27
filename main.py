
import pygame
import file_importer as fi

pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('3D OBJ File Renderer')
clock, fps = pygame.time.Clock(), 30

path = 'normals_test.obj'
shape = fi.load_obj(path, (300, 300), size)
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
    shape.draw_face(screen)

    pygame.display.update()

    if key[pygame.K_SPACE]:
        pygame.image.save(screen, 'Frame/image.png')

    clock.tick(fps)
