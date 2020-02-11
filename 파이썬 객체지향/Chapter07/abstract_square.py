# 예시는 그림판으로
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Sqaure(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.height * self.width

    def perimeter(self) -> float:
        return self.height ** 2 + self.width

    def __str__(self):
        return "둘레는 {}, 넓이는 {}인 사각형입니다.".format(self.area(), self.perimeter())

sqaure = Sqaure(3, 4)

print(sqaure)