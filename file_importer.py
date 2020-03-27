from shape_class import Shape
from assistance_functions import map_from_to

def load_obj(path, plane_size, screen_size, bounding_box=0):
    """
    Loads the OBJ file into a shape class
    <path STRING> = Path to your OBJ
    <plane_size TUPLE> = size of the screen for the object to be drawn to, this will clamp the object size into this range
    <screen_size TUPLE> = the size of the actual pygame screen
    <bounding_box INT> = a buffer that will be subtracted from the plane size
    """

    # load raw lines
    with open(path, 'r') as file:
        raw = file.readlines()

    # load only verts
    verts = []
    faces = []
    texture_verts = []
    normals = []
    for line in raw:
        if line.split(' ')[0].lower() == 'v':
            verts.append(line.replace('v ', ''))

        if line.split(' ')[0].lower() == 'f':
            faces.append(line.replace('f ', ''))

        if line.split(' ')[0].lower() == 'vt':
            texture_verts.append(line.replace('vt ', ''))

        if line.split(' ')[0].lower() == 'vn':
            normals.append(line.replace('vn ', ''))

    highest_x = 0
    lowest_x = 10**10
    highest_y = 0
    lowest_y = 10**10
    highest_z = 0
    lowest_z = 10**10

    # cast all verts to floats
    temp = []
    for vert in verts:
        x, y, z = vert.split(' ')

        x = float(x)
        y = float(y)
        z = float(z)

        if x > highest_x:
            highest_x = x
        if y > highest_y:
            highest_y = y
        if z > highest_z:
            highest_z = z
        if x < lowest_x:
            lowest_x = x
        if y < lowest_y:
            lowest_y = y
        if z < lowest_z:
            lowest_z = z

        temp.append([x, y, z])
    verts = temp

    # map the shape to the screen

    master_low = sorted([lowest_x, lowest_y, lowest_z])[0]
    master_high = sorted([highest_x, highest_y, highest_z])[2]

    temp = []
    for vert in verts:
        x, y, z = vert

        x = map_from_to(x, master_low, master_high, bounding_box, plane_size[0] - bounding_box) - plane_size[0]/2
        y = map_from_to(y, master_low, master_high, bounding_box, plane_size[1] - bounding_box) - plane_size[1]/2
        z = map_from_to(z, master_low, master_high, bounding_box, plane_size[0] - bounding_box) - plane_size[0]/2

        temp.append([x, y, z])
    verts = temp

    # load face verticies
    temp = []
    for face in faces:
        face = face.split(' ')
        f = []
        for i in face:
            f.append(int(i.split('/')[0]))
        temp.append(f)
    faces = temp

    # load texture verticies
    temp = []
    for vert in texture_verts:
        vert = vert.split(' ')

        x = float(vert[0])
        y = float(vert[1])

        temp.append([x, y, 0])
    texture_verts = temp

    # load normals
    temp = []
    for vert in normals:
        x, y, z = vert.split(' ')

        temp.append([float(x), float(y), float(z)])
    normals = temp

    # create and return shape
    return Shape(screen_size, verts, faces, texture_verts, normals)
