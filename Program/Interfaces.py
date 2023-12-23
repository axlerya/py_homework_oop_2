from abc import ABC, abstractmethod

# интерфейс воздушного траспорта


class Flyable(ABC):

    @abstractmethod
    def take_off():  # взлет самолета.
        pass

    @abstractmethod
    def land():  # посадка самолета.
        pass

# интерфейс водного траспорта


class Swimmable(ABC):

    @abstractmethod
    def start_swimming():  # начало движения лодки по воде
        pass

    @abstractmethod
    def stop_swimming():  # прекращение движения лодки по воде
        pass
