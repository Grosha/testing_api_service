import json
import logging
from random import randint

from locust.exception import StopUser

from api_services.rent_car_company import CarStatus, Car, CarType
from locust import HttpUser, between, task, events

logger = logging.getLogger(__name__)


@events.test_start.add_listener
def on_test_start(**kwargs):
    logger.info("A new test is starting")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    logger.info("A new test is ending")


class RentCarOffice(HttpUser):
    weight = 3
    wait_time = between(1, 2)
    list_models_for_removing = ['Accord', 'CLS200', 'Land Cruiser']
    car_list = []

    @task
    def on_start(self):
        with self.client.get("/ping", name='ping') as response:
            if response.status_code != 200:
                logger.critical('Server does not response')
                self.environment.runner.quit()
                # raise StopUser

    @task(2)
    def add_car(self):
        model = f'Accord v{randint(0, 1000)}'
        self.list_models_for_removing.append(model)
        new_car = Car('Honda', model, CarType.SEDAN.value, CarStatus.AVAILABLE.value).get_car_info()
        logger.info(f'new car added {new_car}')
        self.client.post('/car', json=new_car, name='add new car')

    @task
    def get_car(self):
        self.client.get('/car', name='get available car')

    @task
    def return_car(self):
        for car in self.car_list:
            car_ = json.loads(car)
            if car_['status'] == CarStatus.NOT_AVAILABLE.value:
                self.client.patch(f'/car/update/{car_["model"]}', name='return car')
                return

    @task
    def delete_car(self):
        model = self.list_models_for_removing.pop()
        self.client.delete(f'/car/{model}', name='delete car')

    @task(4)
    def get_car_list(self):
        with self.client.get("/car_list", name='get car list') as response:
            self.car_list = response.json().get('message')


class RentCarUser(HttpUser):
    weight = 1
    wait_time = between(1, 2)

    @task
    def on_start(self):
        with self.client.get("/ping", name='ping') as response:
            if response.status_code != 200:
                logger.critical('Server does not response')
                raise StopUser

    @task
    def get_car(self):
        self.client.get('/car', name='get available car')

    @task
    def get_incorrect_car(self):
        model_name = {'model': 'No car'}
        message = 'Car model No car is absent in the list'
        with self.client.get('/car', params=model_name, name='get incorrect car', catch_response=True) as response:
            if message in response.text:
                logger.info(f'new car with model {model_name}')
                # logger.error(f'Server returns not exists car {model_name}')
                # response.failure("Incorrect error message")

    @task(4)
    def get_car_list(self):
        self.client.get("/car_list", name='get car list')
