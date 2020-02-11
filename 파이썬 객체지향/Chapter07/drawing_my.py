from abc import ABC, abstractmethod
from math import pi
from math import ceil


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle의 넓이는 {}입니다.".format(self.area())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
        # return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return "Circle의 둘레는 {}, 넓이는 {} 입니다.".format(self.perimeter(), self.area())


class Triangle():
    def __str__(self):
        return "삼각형"
    pass


class All:
    def __init__(self):
        self.shapes = []

    '''
        #LBYL
        #어떤 작업을 수행하기전에 그 작업을 수행해도 괜찮을지 확인     
        def add_shape(self, shape):
            if isinstance(shape, Shape):
                self.shapes.append(shape)
            else:
                print("값이 잘못됬거나 Shape 클래스에 포함되지 않았습니다.")

        def total_area_shapes(self):
            return "그림판에 있는 모든 도형의 넓이는 {} 입니다.".format(round(sum(total.area() for total in self.shapes), 3))

    '''

    """
        #EAFP
        일단 먼저 빨리 실행하고, 문제가 생기면 처리한다.
    """

    def add_shape(self, shape:Shape):
        self.shapes.append(shape)

    def total_area_shapes(self):
        total_area = 0

        for shape in self.shapes:
            try:
                total_area += shape.area()
            except (AttributeError, TypeError): #AttributeError: 이름이 잘못됐거나 없는 속성
                print("그림판에 area 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}이 있습니다.".format(shape))
        return total_area

    def __str__(self):
        s_info = ""
        for shape_info in self.shapes:
            s_info += str(shape_info) + "\n"
        return s_info

rectangle = Rectangle(4, 5)
circle = Circle(3)
triangle = Triangle()

print(rectangle)
print(circle)


all = All()

all.add_shape(triangle)
all.add_shape(circle)
all.add_shape(rectangle)

print(all.total_area_shapes())
print(all)