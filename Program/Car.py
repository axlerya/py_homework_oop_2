from Program.Vehicle import Vehicle


class Car(Vehicle):
    __engine_is_on = False
    __speed = 0
    __is_driving = False

    def __init__(self, id: int, brand: str, model: str, year: int, fuel_capacity: int, current_fuel_lvl: int):
        super().__init__(id, brand, model, year, fuel_capacity, current_fuel_lvl)

    def get_speed(self):  # чтение и запись приватных полей
        return self.__speed

    def get_is_driving(self):
        return self.__is_driving

    def get_engine_is_on(self):
        return self.__engine_is_on

    def set_speed(self, speed: int):
        self.__speed = speed

    def set_is_driving(self, is_driving: bool):
        self.__is_driving = is_driving

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
        
        

    def acelerate(self, speed: int):
        self.set_speed(speed)
        self.set_is_driving(True)
        return f"""
        {self.start_engine()}
        Автомобиль в пути:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        Скорость - {self.get_speed()}
        """

    def brake(self):
        self.acelerate(0)
        self.set_is_driving(False)
        return f"""
        Автомобиль остановился:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        """

    def refuel(self, value: int):
        super().refuel(value)
        return f"""
        Заправка автомобиля:
        ID - {self.get_id()}
        Объем бака - {self.get_fuel_capacity()}
        Текущий уровень топлива - {self.get_current_fuel_lvl()}
        """

    def displayInfo(self):
        return f"""
        Информация о автомобиле:
        ID - {self.get_id()}
        Brand - {self.get_brand()}
        Model - {self.get_model()}
        Year - {self.get_year()}
        Объем бака - {self.get_fuel_capacity()}
        Текущий уровень топлива - {self.get_current_fuel_lvl()}
        В поездке - {self.get_is_driving()}
        """
