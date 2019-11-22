import pygame
from formater import formatVerti
from math import sin, cos, sqrt
import settings

pygame.init()

size = [700, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')

clock = pygame.time.Clock()
fps = 30

points, order = formatVerti(settings.model_path, settings.zoom)

render_screen = pygame.Surface((700, 700))
render_screen.fill(0)

print '\nPoints {}'.format(len(points))
print 'Orders {}\n'.format(len(order))

def Rotate(points):
    temp = []
    for point in points:
        x, y, z = point

        dx = (cos(settings.spin_speed) * x) + (0 * y) + (sin(settings.spin_speed) * z)
        dy = (0 * x) + (1 * y) + (0 * z)
        dz = (-sin(settings.spin_speed) * x) + (0 * y) + (cos(settings.spin_speed) * z)

        temp.append([dx, dy, dz])

    return temp

def dist_to_color(x, y, z):
    global mouse_pos

    if settings.lightX == -1 and settings.lightY == -1 and settings.lightZ == -1:
        return 255
    elif settings.lightX == 0 and settings.lightY == 0 and settings.lightZ == 0:
        return sqrt((mouse_pos[0] - x)**2 + (mouse_pos[1] - y)**2 + (500 - z)**2) % 255
    else:
        dist_ = sqrt((settings.lightX - x)**2 + (settings.lightY - y)**2 + (settings.lightZ - z)**2)
        if dist_ > 0:
            return dist_ % 255
        else:
            return 0

def dist(x1, y1, z1, x2, y2, z2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def Wire_Frame(render_screen, order, points):
    for i in range(len(order) - 1):
        try:
            point1 = points[order[i][0]]
            point2 = points[order[i][1]]
            point3 = points[order[i][2]]

            polygon = [
                (point1[0] + settings.offsetX, point1[1] + settings.offsetY),
                (point2[0] + settings.offsetX, point2[1] + settings.offsetY),
                (point3[0] + settings.offsetX, point3[1] + settings.offsetY)
            ]

            color = dist_to_color(point3[0], point3[1], point3[2])

            pygame.draw.polygon(render_screen, [color, color, color], polygon, 1)
        except IndexError:
            pass

def ReturnDist(elem):
    x, y, z = elem[0]
    return dist(x, y, z, 350, 350, 1000)

def Face_View(render_screen, order, points):
    to_draw = []
    for i in range(len(order) - 1):
        if len(order[i]) == 3:
            try:
                point1 = points[order[i][0]]
                point2 = points[order[i][1]]
                point3 = points[order[i][2]]

                polygon = [
                    (point1[0] + settings.offsetX, point1[1] + settings.offsetY, point1[2]),
                    (point2[0] + settings.offsetX, point2[1] + settings.offsetY, point2[2]),
                    (point3[0] + settings.offsetX, point3[1] + settings.offsetY, point3[2])
                ]

                to_draw.append(polygon)
            except IndexError:
                pass
        elif len(order[i]) == 4:
            try:
                point1 = points[order[i][0]]
                point2 = points[order[i][1]]
                point3 = points[order[i][2]]
                point4 = points[order[i][3]]

                polygon = [
                    (point1[0] + settings.offsetX, point1[1] + settings.offsetY, point1[2]),
                    (point2[0] + settings.offsetX, point2[1] + settings.offsetY, point2[2]),
                    (point3[0] + settings.offsetX, point3[1] + settings.offsetY, point3[2]),
                    (point4[0] + settings.offsetX, point4[1] + settings.offsetY, point4[2])
                ]

                to_draw.append(polygon)
            except IndexError:
                pass


    to_draw.sort(key=ReturnDist, reverse=True)

    for draw in to_draw:
        
        average_x = (draw[0][0] + draw[1][0] + draw[2][0]) / 3
        average_y = (draw[0][1] + draw[1][1] + draw[2][1]) / 3
        average_z = (draw[0][2] + draw[1][2] + draw[2][2]) / 3

        color = dist_to_color(average_x, average_y, average_z)

        temp = []
        for pol in draw:
            temp.append((pol[0], pol[1]))
        draw = temp

        if color != 0:
            pygame.draw.polygon(render_screen, [color, color, color], draw, 0)

def Vertex_View(render_screen, order, points):
    for point in points:
        x = int(round(point[0], 0)) + settings.offsetX
        y = int(round(point[1], 0)) + settings.offsetY
        z = int(round(point[2], 0))

        color = dist_to_color(x, y, z)

        pygame.draw.circle(render_screen, [color, color, color], (x, y), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    global mouse_pos
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()

    screen.fill(0)
    render_screen.fill(0)
    
    if settings.render_mode == 1:
        Wire_Frame(render_screen, order, points)    
    elif settings.render_mode == 2:
        Face_View(render_screen, order, points)
    else:
        Vertex_View(render_screen, order, points)

    points = Rotate(points)

    render_screen = pygame.transform.rotate(render_screen, 180)
    screen.blit(render_screen, (0, 0))

    pygame.display.update()
    clock.tick(fps)

