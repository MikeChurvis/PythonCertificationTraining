import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        offset_x = self.__x - x
        offset_y = self.__y - y
        return math.hypot(offset_x, offset_y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertices = vertice1, vertice2, vertice3

    def perimeter(self):
        return sum(
            self.vertices[i].distance_from_point(
                self.vertices[(i + 1) % len(self.vertices)]
            )
            for i in range(len(self.vertices))
        )


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
