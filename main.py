# Add python code in this file
import csv


class City:
    def __init__(self, name, topleftx, toplefty, bottomrightx, bottomrighty):
        self.name = name
        self.topleftx = topleftx
        self.toplefty = toplefty
        self.bottomrightx = bottomrightx
        self.bottomrighty = bottomrighty


class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


# make a list of Cities
CityList = []
with open('cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} is from ({row[1]},{row[2]}) to ({row[3]},{row[4]})')
            CityList.append(City(row[0], row[1], row[2], row[3], row[4]))
            line_count += 1
    print(f'Processed {line_count} lines.')


# make a list of points
PointList = []
with open('points.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            PointList.append(Point(row[0], row[1], row[2]))
            line_count += 1
    print(f'Processed {line_count} lines.')

with open('output_points.csv', mode='w') as point_file:
    point_writer = csv.writer(point_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    point_writer.writerow(['ID', 'X', 'Y', 'Inside'])
    for pt in PointList:
        inside = None
        for ct in CityList:
            # check if point p is in the city or not
            ax = int(ct.topleftx)
            ay = int(ct.toplefty)
            cx = int(ct.bottomrightx)
            cy = int(ct.bottomrighty)
            bx = cx
            by = ay
            dx = ax
            dy = cy
            px = int(pt.x)
            py = int(pt.y)
            # rectangle of 4 points
            # calculate area of the rectangle
            areaRectangle = 0.5 * abs((ay - cy) * (dx - bx) + (by - dy) * (ax - cx))
            # calculate the area of the triangles apb, bpc, cpd, dpa
            # area of apb is a1
            a1 = 0.5 * abs(ax * (py - by) + px * (by - ay) + bx * (ay - py))
            # area of bpc is a2
            a2 = 0.5 * abs(bx * (py - cy) + px * (cy - by) + cx * (by - py))
            # area of cpd is a3
            a3 = 0.5 * abs(cx * (py - dy) + px * (dy - cy) + dx * (cy - py))
            # area of dpa is a4
            a4 = 0.5 * abs(dx * (py - ay) + px * (ay - dy) + ax * (dy - py))
            if a1 + a2 + a3 + a4 == areaRectangle:
                inside = ct.name
                break
            else:
                inside = None
        if inside is None:
            point_writer.writerow([pt.id, pt.x, pt.y, 'None'])
        else:
            point_writer.writerow([pt.id, pt.x, pt.y, inside])
