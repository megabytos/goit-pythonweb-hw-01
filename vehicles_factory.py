from abc import ABC, abstractmethod
from typing import Optional
import logging

logging.basicConfig(
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: Optional[str] = None) -> None:
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {'(' + self.region + ' Spec)' if self.region else ''}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {'(' + self.region + ' Spec)' if self.region else ''}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


if __name__ == "__main__":
    vehicle1 = Car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = Motorcycle("Ducati", "Multistrada")
    vehicle2.start_engine()

    us_factory = USVehicleFactory()
    us_vehicle = us_factory.create_car("Ford", "Fusion")
    us_vehicle.start_engine()
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_motorcycle.start_engine()

    eu_factory = EUVehicleFactory()
    eu_vehicle = eu_factory.create_car("Ford", "Fusion")
    eu_vehicle.start_engine()
    eu_motorcycle = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    eu_motorcycle.start_engine()
