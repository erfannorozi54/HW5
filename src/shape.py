import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def length(self) -> int:
        return math.sqrt(self.x**2 + self.y**2)


class Shape:
    def __init__(self, *args) -> None:
        self.vertices = []
        for i in args:
            self.vertices.append(i)

    def add_vertex(self, p: Point) -> None:
        self.vertices.append(p)

    def __str__(self) -> str:
        return f"number of vertices: {len(self.vertices)}"

    def perimeter(self) -> float:
        if not len(self.vertices):
            raise RuntimeError()
        temp = self.vertices[len(self.vertices)-1]
        perimeter = 0
        for i in self.vertices:
            perimeter += math.sqrt((i.x - temp.x)**2 + (i.y - temp.y)**2)
            temp = i
        if len(self.vertices) == 2:
            perimeter /= 2
        return perimeter


class Line(Shape):
    def __init__(self, p1: Point, p2: Point) -> None:
        super().__init__(p1, p2)

    def __str__(self) -> str:
        return f"p1: (x: {self.vertices[0].x}, y: {self.vertices[0].y})\np2: (x: {self.vertices[1].x}, y:{self.vertices[1].y})"

    def area(self) -> float:
        return 0


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        super().__init__(p1, p2, p3)
        if self.area() == 0:
            raise RuntimeError

    def __str__(self) -> str:
        return f"p1: (x: {self.vertices[0].x}, y: {self.vertices[0].y})\np2: (x: {self.vertices[1].x}, y:{self.vertices[1].y})\np2: (x: {self.vertices[2].x}, y:{self.vertices[2].y})"

    def area(self) -> float:
        try:
            m_line1 = (self.vertices[0].y-self.vertices[1].y) / \
                (self.vertices[0].x-self.vertices[1].x)
            theta1 = math.atan(m_line1)
        except ZeroDivisionError:
            theta1 = math.pi/2
        try:
            m_line2 = (self.vertices[2].y-self.vertices[1].y) / \
                (self.vertices[2].x-self.vertices[1].x)
            theta2 = math.atan(m_line2)
        except ZeroDivisionError:
            theta2 = math.pi/2
        theta = abs(theta1 - theta2)
        length_line1 = math.sqrt(
            (self.vertices[0].x-self.vertices[1].x)**2 + (self.vertices[0].y-self.vertices[1].y)**2)
        length_line2 = math.sqrt(
            (self.vertices[2].x-self.vertices[1].x)**2 + (self.vertices[2].y-self.vertices[1].y)**2)
        return length_line1*length_line2*math.sin(theta)*0.5

class Rectangle(Shape):
    def __init__(self, p1: Point, p2: Point) -> None:
        super().__init__(p1, p2)

    def __str__(self) -> str:
        return f"p1: (x: {self.vertices[0].x}, y: {self.vertices[0].y})\np2: (x: {self.vertices[1].x}, y:{self.vertices[0].y})\np3: (x: {self.vertices[1].x}, y:{self.vertices[1].y})\np4: (x: {self.vertices[0].x}, y:{self.vertices[1].y})"

    def area(self) -> float:
        return 0.5*((self.vertices[0].x-self.vertices[1].x)**2+(self.vertices[0].y-self.vertices[1].y)**2)


if __name__ == "__main__":
    x = [1,2,3,4,5,6]
    print(x[len(x)-1])
