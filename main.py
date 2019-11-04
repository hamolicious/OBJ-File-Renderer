import pygame
from point import Point
from controlls import *
from math import sqrt
from time import time as epoh
from sys import argv
from colorama import Fore, Style

pygame.init()
pygame.display.init()
pygame.font.init()

size = [1300, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')

clock = pygame.time.Clock()
fps = 30

# zooms model in
zoom = 1

# offsets x axis
offsetX = 350

# offsets y axis
offsetY = 350

# normalises points
multip = 10

def FormatPoints(points):
    temp = []

    for point in points:
        try:
            if point[0] + point[1] == 'v ':
                vertex = point.split(' ')

                for verti in vertex:
                    verti = verti.strip()
                    verti = verti.replace('  ', '')

                temp.append(vertex)
        except IndexError:
            pass

    return temp

def LoadModel(multip):
    try:
        file = open(str(argv[1]))
    except IndexError:
        print( Fore.GREEN + Style.BRIGHT + '\nTry adding the obj file to the end of the python command\n' + Style.RESET_ALL)
        quit(1)
    points = file.readlines()
    file.close()

    points = FormatPoints(points)

    temp = []

    for point in points:
        x = int(round(float(point[1]) * multip, 0))
        y = int(round(float(point[2]) * multip, 0))
        z = int(round(float(point[3]) * multip, 0))

        temp.append(Point(x, y, z))

    return temp

def Spin(points):
    for point in points:

        if point.x + offsetX > 350:
            point.x -= 2
        elif point.x + offsetX < 350:
            point.x += 2

    return points

def Render(points, i):
    canvas = pygame.Surface((700, 700))
    canvas.fill(0)

    if shouldSpin.boolean:
        points = Spin(points)
    else:
        points = LoadModel(multip)
    
    for point in points:
        if shouldScroll.boolean:
            if point.z == i:
                pygame.draw.rect(canvas, [255, 255, 255], point.returnRect(zoom, offsetX, offsetY), 0)
        else:
            pygame.draw.rect(canvas, [255, 255, 255], point.returnRect(zoom, offsetX, offsetY), 0)

    if shouldLinealise.boolean:
        for i in range(len(points) - 1):
            a = (points[i].x * zoom + offsetX, points[i].y * zoom + offsetY)
            b = (points[i + 1].x * zoom + offsetX, points[i + 1].y * zoom + offsetY)
            pygame.draw.line(canvas, [200, 200, 200], a, b, 1)

    canvas = pygame.transform.rotate(canvas, 180)

    return canvas

points = LoadModel(multip)

lowestZ = 10**10
highestZ = 0
for point in points:
    if point.z > highestZ:
        highestZ = point.z

    if point.z < lowestZ:
        lowestZ = point.z
i = highestZ

y = 10
shouldScroll = CheckBox(710, y, 20, 'Scroll Through Layers', 'ariel')
y += 25
shouldSpin = CheckBox(710, y, 20, 'Spin (BROKEN)', 'ariel')
y += 25
shouldLinealise = CheckBox(710, y, 20, 'Add Lines', 'ariel')
y += 30
incXOffBtn = Button(710, y, 2, '+ X Offset', 'ariel')
y += 25
decXOffBtn = Button(710, y, 2, '- X Offset', 'ariel')
y += 30
incYOffBtn = Button(710, y, 2, '+ Y Offset', 'ariel')
y += 25
decYOffBtn = Button(710, y, 2, '- Y Offset', 'ariel')
y += 30
incZoom = Button(710, y, 2, '+ Zoom', 'ariel')
y += 25
decZoom = Button(710, y, 2, '- Zoom', 'ariel')
y += 30
incMultip = Button(710, y, 2, '+ Multiplier', 'ariel')
y += 25
decMultip = Button(710, y, 2, '- Multiplier', 'ariel')
y += 30

font = pygame.font.SysFont('ariel', 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()

    screen.fill([20, 20, 20])

    renderMark = epoh()
    screen.blit(Render(points, i), (0, 0))
    renderMark -= epoh()

    shouldScroll.update(screen, mouse_pos, mouse_pressed)
    shouldSpin.update(screen, mouse_pos, mouse_pressed)
    shouldLinealise.update(screen, mouse_pos, mouse_pressed)

    # region Controlls Logic
    if incXOffBtn.update(screen, mouse_pos, mouse_pressed):
        offsetX += 10
    
    if decXOffBtn.update(screen, mouse_pos, mouse_pressed):
        offsetX -= 10
    
    if incYOffBtn.update(screen, mouse_pos, mouse_pressed):
        offsetY += 10
    
    if decYOffBtn.update(screen, mouse_pos, mouse_pressed):
        offsetY -= 10
    

    if incZoom.update(screen, mouse_pos, mouse_pressed):
        zoom += 0.25
    
    if decZoom.update(screen, mouse_pos, mouse_pressed):
        zoom -= 0.25


    if incMultip.update(screen, mouse_pos, mouse_pressed):
        multip += 2
        points = LoadModel(multip)
    
    if decMultip.update(screen, mouse_pos, mouse_pressed):
        multip -= 2
        points = LoadModel(multip)
    #endregion

    i -= 1
    if i < lowestZ:
        i = highestZ

    screen.blit(font.render('Time to Render Frame  {}ms'.format(round(renderMark, 5) * -1000), 1, [255, 255, 255]), (710, 500))
    screen.blit(font.render('Time to Render Vertex  {}ms'.format((round(renderMark, 5) / len(points)) * -1000), 1, [255, 255, 255]), (710, 530))
    screen.blit(font.render('Vertex on Screen  {}'.format(len(points)), 1, [255, 255, 255]), (710, 560))

    pygame.display.update()
    clock.tick(fps)

