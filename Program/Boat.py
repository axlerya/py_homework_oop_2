from Program.Vehicle import Vehicle
from Program.Interfaces import Swimmable


class Boat(Vehicle, Swimmable):
    __is_sailing = False
    __engine_is_on = False

    def __init__(self, id: int, brand: str, model: str, year: int, fuel_capacity: int, current_fuel_lvl: int):
        super().__init__(id, brand, model, year, fuel_capacity, current_fuel_lvl)

    def get_is_sailing(self):  # чтение и запись приватных полей
        return self.__is_sailing
    
    def get_engine_is_on(self):
        return self.__engine_is_on

    def set_is_sailing(self, is_sailing: bool):
        self.__is_sailing = is_sailing
        
    def set_engine_is_on(self, engine_is_on: bool):
        self.__engine_is_on = engine_is_on

    def start_engine(self):
        if self.get_engine_is_on() == True:
            return
        else:
            self.set_engine_is_on(True)
            return f"Запущен двигатель у ID {self.get_id()}"

    def stop_engine(self):
        if self.get_engine_is_on() == False:
            return
        else:
            self.set_engine_is_on(False)
            return f"Остановлен двигатель у ID {self.get_id()}"

    def start_swimming(self):
        self.set_is_sailing(True)
        return f"""
        {self.start_engine()}
        Лодка в пути:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        """

    def stop_swimming(self):
        self.set_is_sailing(False)
        return f"""
        Лодка остановилась:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        """

    def refuel(self, value: int):
        super().refuel(value)
        return f"""
        Заправка лодки:
        ID - {self.get_id()}
        Объем бака - {self.get_fuel_capacity()}
        Текущий уровень топлива - {self.get_current_fuel_lvl()}
        """

    def displayInfo(self):
        return f"""
        Информация о лодке:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        Year - {self.get_year()}
        Объем бака - {self.get_fuel_capacity()}
        Текущий уровень топлива - {self.get_current_fuel_lvl()}
        В поездке - {self.get_is_sailing()}
        """
