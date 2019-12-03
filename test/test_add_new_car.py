import json

import requests

from settings.services import API


class TestAddNewCar:
    def test_add_new_car(self):
        requests.post(API().car(), data='{"name":"Lamborghini", "model":"Huracan", "type":"sportcar", "status":1}')
        car = json.load(requests.get(API().car() + f'?model=Huracan')).get('massage')
        assert car.get_name() is 'Lamborghini'
