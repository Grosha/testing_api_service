import json
import re

import requests
from pytest import fixture

from settings.services import API


class TestGetCar:

    def test_get_car(self):
        car = json.load(requests.get(API().car())).get('massage')
        re.match('.+', car.get('name'))
        re.match('.+', car.get('model'))
        re.match('.+', car.get('type'))
        re.match('\d+', car.get('status'))

    @fixture(scope="function", autouse=False)
    def rent_all_car(self):
        car_list = json.load(requests.get(API().car_list())).get('massage')
        for car in car_list:
            requests.patch(API().update_car_detail(car.get_model()) + f'?status=0')
        yield
        for car in car_list:
            requests.patch(API().update_car_detail(car.get_model()) + f'?status=1')

    def test_get_car_when_no_available(self, rent_all_car):
        expected_message = 'No free car available'
        actual_message = json.load(requests.get(API().car())).get('massage')
        assert actual_message is expected_message, f'Incorrect message when all car are absent:\n {actual_message} but must be\n {expected_message}'
