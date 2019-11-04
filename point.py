import pygame

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def returnRect(self, zoom, offsetX, offsetY):
        x = self.x * zoom
        y = self.y * zoom
        return pygame.Rect(x + offsetX, y + offsetY, 1, 1)
