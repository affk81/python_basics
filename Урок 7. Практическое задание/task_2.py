"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def coat_calc(self):
        pass

    @abstractmethod
    def suit_calc(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, param):
        self.param = param

    @property
    def coat_calc(self):
        return self.param / 6.5 + 0.5

    @property
    def suit_calc(self):
        return self.param * 2 + 0.3


my_coat = Clothes(52)
my_suit = Clothes(1.8)
print(f"Расход ткани на пальто: {my_coat.coat_calc}")
print(f"Расход ткани на костюм: {my_suit.suit_calc}")
print(f"Общий расход ткани: {my_coat.coat_calc + my_suit.suit_calc}")
