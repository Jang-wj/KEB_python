import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def get_area(self):
        print('면적을 출력합니다')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, x, y, width, lenght):
        super().__init__(x, y)
        self.width = width
        self.lenght = lenght

    def get_area(self):
        return self.width * self.lenght

    def __repr__(self):
        return f'사각형의 좌표는 ({self.x}, {self.y}) 넓이는 {self.width * self.lenght} 입니다.'

    def __add__(self, other):
        # 두 사각형 넓이의 합
        # return self.width * self.lenght + other.width * other.lenght
        # 각 사각형의 width의 합과 lenght의 합의 곱
        return Rectangle(0, 0, self.width+other.width, self.lenght+other.lenght)

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height

    def get_area(self):
        return super().get_area() * self.height


c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(70, 30, 20, 5)

cy1 = Cylinder(100, 10, 10.0, 2)

print(c1.get_area())
print(c2.get_area())
print(r1)
print(r2)
print(cy1.get_area())
print(r1 + r2)

# 매직 매서드 = 연산자 오버라이딩

