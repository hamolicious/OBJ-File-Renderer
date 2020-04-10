from math import sin, cos, sqrt

class Vector():
    def __init__(self, x, y, z):

        if str in [type(x), type(y), type(z)]:
            print('\n', x,y,z)
            raise ValueError('Can only be numerical values')

        self.x = x
        self.y = y
        self.z = z

        self.texture = None

        self.id = None

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def div(self, other):
        self.x /= other
        self.y /= other
        self.z /= other

    def mult(self, other):
        self.x /= other
        self.y /= other
        self.z /= other

    def get_xy(self, return_true=False):
        if return_true:
            return (self.x, self.y)
        
        return (int(self.x), int(self.y))

    def get_xy_center(self, size):
        return (int(self.x + size[0]/2), int(self.y + size[1]/2))

    def rotate_x(self, a):
        self.x = (1 * self.x) + (0 * self.y) + (0 * self.z)
        self.y = (0 * self.x) + (cos(a) * self.y) + (-sin(a) * self.z)
        self.z = (0 * self.x) + (sin(a) * self.y) + (cos(a) * self.z)

    def rotate_y(self, a):
        self.x = (cos(a) * self.x) + (0 * self.y) + (sin(a) * self.z)
        self.y = (0 * self.x) + (1 * self.y) + (0 * self.z)
        self.z = (-sin(a) * self.x) + (0 * self.y) + (cos(a) * self.z)

    def rotate_z(self, a):
        self.x = (cos(a) * self.x) + (-sin(a) * self.y) + (0 * self.z)
        self.y = (sin(a) * self.x) + (cos(a) * self.y) + (0 * self.z)
        self.z = (0 * self.x) + (0 * self.y) + (1 * self.z)

