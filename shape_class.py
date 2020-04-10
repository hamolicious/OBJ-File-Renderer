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

def assign_id(vectors):
    i = 0
    for vec in vectors:
        vec.id = i
        i += 1
    return vectors

def add_colors(*colours):
    total_color = [0, 0, 0]
    for color in colours:
        total_color[0] += color[0]
        total_color[1] += color[1]
        total_color[2] += color[2]

    return total_color

class Shape():
    def __init__(self, size, verts, faces, texture_verts, normals):
        self.size = size

        self.verts = assign_id(vectorise_data(verts))
        self.faces = faces
        self.texture_verts = vectorise_data(texture_verts)

        self.draw_averages = False
        self.average_size = 5
        self.draw_normals = False

        self.texture = pygame.image.load('C:/Users/User/Desktop/pallete.png')
        self.texture = pygame.transform.flip(self.texture, False, True)

        for vert, text_vert in zip(self.verts, self.texture_verts):
            text_vert.x *= self.texture.get_width()
            text_vert.y *= self.texture.get_height()

            color = self.texture.get_at((text_vert.get_xy()))
            vert.texture = color

        self.normals = []
        for norm in vectorise_data(normals):
            norm.mult(-1)
            self.normals.append(norm)

    def flip(self):
        """Flips the model 180 degrees (1 PI radians), sometimes OBJ files are exported upside down"""
        for vert in self.verts:
            vert.rotate_x(pi)

    def rotate(self, x=0, y=0.01, z=0):
        """Rotates the model around it's local center, arguments are specified in radians"""
        for vert in self.verts:
            vert.rotate_x(x)
            vert.rotate_y(y)
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
            pygame.draw.circle(screen, vert.texture, vert.get_xy_center(self.size), 2)

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
                return ((0 - avrg.x)**2 + (0 - avrg.y)**2 + (-10000 - avrg.z)**2)
            else:
                return 0

        polygons = []
        for vert in self.faces:
            polygon = []
            for i in vert:
                polygon.append(self.verts[i-1])

            polygons.append(polygon)

        for face in sorted(polygons, key=dist):
            polygon = []
            avrg_color = [0, 0, 0]
            for vert in face:
                polygon.append(vert.get_xy_center(self.size))
                avrg_color = add_colors(avrg_color, vert.texture)
            
            # get the average colour of the texture
            avrg_color[0] /= len(face)
            avrg_color[1] /= len(face)
            avrg_color[2] /= len(face)

            pygame.draw.polygon(screen, avrg_color, polygon)

        if self.draw_averages:
            for average in averages:
                pygame.draw.circle(screen, [255, 0, 0], average.get_xy_center(self.size), self.average_size)

        if self.draw_normals:
            for average, normal in zip(averages, self.normals):
                pos = average - normal
                pos.mult(2)
                pygame.draw.line(screen, [0, 255, 0], average.get_xy_center(self.size), pos.get_xy_center(self.size), 3)
