import json
import re

import requests

from settings.services import API


class TestGetCar:

    def test_get_car(self):
        car = json.load(requests.get(API().car())).get('massage')
        re.match('.+', car.get('name'))
        re.match('.+',car.get('model'))
        re.match('.+',car.get('type'))
        re.match('.+',car.get('status'))
