"""
В Python нет абстакции реализованной "из коробки". Погуглив и пошарив просторы интернета понял , что в Python,
из-за его динамической природы, явных интерфейсов нет, но они могут быть эмулированы с помощью различных приемов.
А так же что абстракция не особо нужна в Python т.к присутствует множественное наследование ( я могу быть не прав,
говорить с увереностью не могу). Но нашел абстрактные классы и интерфесы в библеотеке ABC (Abstract Base Classes) 
реализованные с помощью декораторов
"""

from abc import ABC, abstractmethod

# Абстрактный класс


class Vehicle(ABC):
    def __init__(self, id: int, brand: str, model: str, year: int, fuel_capacity: int, current_fuel_lvl: int):
        self.__id = id  # уникальный номер
        self.__brand = brand  # бренд
        self.__model = model  # модель
        self.__year = year  # год выпуска
        self.__fuel_capacity = fuel_capacity  # объем топливного бака
        self.__current_fuel_lvl = current_fuel_lvl  # текущий уровень топлива
        super().__init__()

    # чтение приватных переменных
    def get_id(self):
        return self.__id

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_fuel_capacity(self):
        return self.__fuel_capacity

    def get_current_fuel_lvl(self):
        return self.__current_fuel_lvl

    # запись приватных переменных
    def set_id(self, id: int):
        self.__id = id

    def set_brand(self, brand: str):
        self.__brand = brand

    def set_model(self, model: str):
        self.__model = model

    def set_year(self, year: int):
        self.__year = year

    def set_fuel_capacity(self, fuel_capacity: int):
        self.__fuel_capacity = fuel_capacity

    def set_current_fuel_lvl(self, current_fuel_lvl: int):
        self.__current_fuel_lvl = current_fuel_lvl
    # Абстрактные методы класса

    @abstractmethod
    def start_engine():  # запуск двигателя
        pass

    @abstractmethod
    def stop_engine():  # остановка двигателя
        pass

    @abstractmethod
    def displayInfo():  # вывод информации
        pass

    @abstractmethod
    def refuel(self, value: int):  # заправка
        if (self.get_fuel_capacity() - self.get_current_fuel_lvl()) >= value:
            return self.set_current_fuel_lvl(self.get_current_fuel_lvl() + value)
        else:
            return self.set_current_fuel_lvl(self.get_fuel_capacity())
