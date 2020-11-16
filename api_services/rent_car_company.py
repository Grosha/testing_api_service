import json
from enum import Enum
from json import JSONEncoder


class CarEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Car:
    def __init__(self, name, model, type, status):
        self.name = name
        self.model = model
        self.type = type
        self.status = status

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_status(self):
        return self.status

    def get_car_info(self):
        car_info = f'"name": "{self.name}", "model": "{self.model}", "type": "{self.type}", "status": {self.status}'
        # print('{' + car_info + '}')
        # return json.loads('{' + car_info + '}')
        return CarEncoder().encode(self)


class CarStatus(Enum):
    AVAILABLE = 1
    NOT_AVAILABLE = 0


class CarType(Enum):
    SEDAN = 'Sedan'
    CROSSOVER = 'Crossover'
    JEEP = 'Jeep'
    SPORT_CAR = 'Sportcar'


# list_cars = {
#     0: (Car('Ford', 'Focus', 'Sedan', 1)),
#     1: (Car('Ford', 'Mustang', 'Sedan', 1)),
#     2: (Car('Honda', 'Accord', 'Sedan', 1)),
#     3: (Car('Honda', 'CRV', 'Crossover', 1)),
#     4: (Car('Honda', 'Civic', 'Sedan', 1)),
#     5: (Car('Lexus', 'IS250', 'Sedan', 1)),
#     6: (Car('Mercedes', 'CLS200', 'Sedan', 1)),
#     7: (Car('Mercedes', 'A180', 'Sedan', 1)),
#     8: (Car('Lexus', 'RX350', 'Crossover', 1)),
#     9: (Car('Toyota', 'Land Cruiser', 'Jeep', 1)),
#     10: (Car('Toyota', 'Land Prado', 'Jeep', 1)),
# }

list_cars = {
    Car('Ford', 'Focus', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Ford', 'Mustang', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Honda', 'Accord', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Honda', 'CRV', CarType.CROSSOVER.value, CarStatus.AVAILABLE.value),
    Car('Honda', 'Civic', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Lexus', 'IS250', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Mercedes', 'CLS200', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Mercedes', 'A180', CarType.SEDAN.value, CarStatus.AVAILABLE.value),
    Car('Lexus', 'RX350', CarType.CROSSOVER.value, CarStatus.AVAILABLE.value),
    Car('Toyota', 'Land Cruiser', CarType.JEEP.value, CarStatus.AVAILABLE.value),
    Car('Toyota', 'Land Prado', CarType.JEEP.value, CarStatus.AVAILABLE.value)
}


def get_value_list_cars():
    value_list_cars = []
    # [value_list_cars.append(list_cars.get(i).get_car_info()) for i in range(len(list_cars))]
    for car in list_cars:
        value_list_cars.append(car.get_car_info())

    return value_list_cars
