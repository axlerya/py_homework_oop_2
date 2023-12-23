from Program.Vehicle import Vehicle
from Program.Interfaces import Flyable


class Aircraft(Vehicle, Flyable):
    __engine_is_on = False
    __is_flying = False

    def __init__(self, id: int, brand: str, model: str, year: int, fuel_capacity: int, current_fuel_lvl: int, max_altitude: int):
        self.__max_altitude = max_altitude
        super().__init__(id, brand, model, year, fuel_capacity, current_fuel_lvl)

    def get_max_altitude(self):
        return self.__max_altitude

    def get_is_flying(self):
        return self.__is_flying
    
    def get_engine_is_on(self):
        return self.__engine_is_on

    def set_max_altitude(self, max_altitude: int):
        self.__max_altitude = max_altitude

    def set_is_flying(self, is_flying: bool):
        self.__is_flying = is_flying
        
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
        
        

    def take_off(self):
        self.set_is_flying(True)
        return f"""
        Взлет воздушного судна:
        {self.start_engine()}
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        """

    def land(self):
        self.set_is_flying(False)
        return f"""
        Посадка воздушного судна:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        {self.stop_engine()}
        """

    def displayInfo(self):
        return f"""
        Информация о воздушном судне:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        Year - {self.get_year()}
        Объем бака - {self.get_fuel_capacity()}
        Текущий уровень топлива - {self.get_current_fuel_lvl()}
        Максимальная высота полета - {self.get_max_altitude()}
        В полете - {self.get_is_flying()}
        """

    def refuel(self, value: int):
        super().refuel(value)
        return f"""
        Заправка воздушного судна:
        ID - {self.get_id()}
        Объем бака - {self.get_fuel_capacity()}
        Текущий уровень топлива - {self.get_current_fuel_lvl()}
        """
