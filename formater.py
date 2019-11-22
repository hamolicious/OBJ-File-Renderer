def formatVerti(modelPath, zoom):
    with open(modelPath, 'r') as file:
        # create order and points lists
        order = []
        points = []

        # grab every point
        for point in file.readlines():
            # check if the point is a vertex
            try:
                if point[0] + point[1] == 'v ':
                    points.append(point.strip(' ').replace('\n', '').replace('v ', ''))
            except IndexError:
                pass    

            try:
                if point[0] + point[1] == 'f ':
                    order.append(point.strip(' ').replace('\n', '').replace('f ', ''))
            except IndexError:
                pass    

        # split points
        temp = []
        for point in points:
            split_temp = []
            for i in point.split(' ') : split_temp.append(float(i))

            temp.append(split_temp)
        points = temp

        # split points
        temp = []
        for point in order:
            split_temp = []
            for i in point.split(' ') : split_temp.append(int(i))

            temp.append(split_temp)
        order = temp

        # offset and zoom points
        temp = []
        for point in points:
            x, y, z = point

            x *= zoom
            y *= zoom
            z *= zoom

            temp.append([x, y, z])
        points = temp
        
        return points, order
