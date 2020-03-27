from data_structures import Vector
from assistance_functions import map_from_to
import pygame
from random import randint
from math import pi

def vectorise_data(raw):
    """Converts a list of [x,y,z] data to Vector(x,y,z)"""
    temp = []
    for vert in raw:
        temp.append(Vector(vert[0], vert[1], vert[2]))

    return temp

class Shape():
    def __init__(self, size, verts, faces, texture_verts, normals):
        self.size = size

        self.verts = vectorise_data(verts)
        self.faces = faces
        self.texture_verts = vectorise_data(texture_verts)

        self.draw_averages = False
        self.average_size = 5
        self.draw_normals = False

        for vert in self.verts:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            vert.texture = [r, g, b]

        self.normals = []
        for norm in vectorise_data(normals):
            norm.mult(-1)
            self.normals.append(norm)

    def flip(self):
        """Flips the model 180 degrees (1 PI radians), sometimes OBJ files are exported upside down"""
        for vert in self.verts:
            vert.rotate_x(pi)

    def rotate(self, x, y, z):
        """Rotates the model around it's local center, arguments are specified in radians"""
        for vert in self.verts:
            vert.rotate_x(x)

        for vert in self.verts:
            vert.rotate_y(y)

        for vert in self.verts:
            vert.rotate_z(z)

    def draw_line(self, screen):
        """Draws the shape as a mesh of lines between the verticies"""
        for vert in self.faces:
            polygon = []
            for i in vert:
                polygon.append(self.verts[i-1].get_xy_center(self.size))
                color = self.verts[i-1].texture
            
            pygame.draw.lines(screen, color, True, polygon)

    def draw_point(self, screen):
        """Draws the shape as a set of unconected verticies"""
        for vert in self.verts:
            pygame.draw.circle(screen, [255, 255, 255], vert.get_xy_center(self.size), 2)

    def draw_face(self, screen, depth_test=True):
        """Draws the shape as a set of faces, depth check is turned on by default, should you need to disable it, pass in depth_test=False"""
        averages = []
        def dist(elem):
            avrg = Vector(0,0,0)
            for vert in elem:
                avrg.add(vert)
            avrg.div(len(elem))

            averages.append(avrg)

            if depth_test:
                return ((0 - avrg.x)**2 + (0 - avrg.y)**2 + (-1000 - avrg.z)**2)
            else:
                return 0

        polygons = []
        for vert in self.faces:
            polygon = []
            for i in vert:
                polygon.append(self.verts[i-1])

            polygons.append(polygon)

        for verts in sorted(polygons, key=dist):
            polygon = []
            for i in verts:
                polygon.append(i.get_xy_center(self.size))
                color = verts[0].texture

            pygame.draw.polygon(screen, color, polygon)

        if self.draw_averages:
            for average in averages:
                pygame.draw.circle(screen, [255, 0, 0], average.get_xy_center(self.size), self.average_size)

        if self.draw_normals:
            for average, normal in zip(averages, self.normals):
                pos = average - normal
                pos.mult(2)
                pygame.draw.line(screen, [0, 255, 0], average.get_xy_center(self.size), pos.get_xy_center(self.size), 3)

