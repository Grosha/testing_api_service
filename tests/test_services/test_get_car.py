import re

import pytest

from settings.services import car_api_service


class TestGetCar:

    def test_get_car(self):
        car = car_api_service.get_car().get('message')
        re.match('.+', car.get('name'))
        re.match('.+', car.get('model'))
        re.match('.+', car.get('type'))
        re.match('\d+', str(car.get('status')))

    def test_get_car_by_model(self):
        expected_car_information = car_api_service.get_car(model='Accord').get('message')
        actual_car_information = {'model': 'Accord', 'name': 'Honda', 'status': 1, 'type': 'Sedan'}

        assert expected_car_information == actual_car_information, f'Incorrect car information for model:' \
            f'\n{expected_car_information}, must be\n{actual_car_information}'

    @pytest.fixture(scope="function", autouse=False)
    def rent_all_car(self):
        car_list = car_api_service.get_car_list().get('message')
        car_api_service.get_car()

        for car in car_list:
            car_api_service.update_car(model=car.get('model'), parameter='status=0')
        yield
        for car in car_list:
            car_api_service.update_car(model=car.get('model'), parameter='status=1')

    def test_get_car_when_no_available(self, rent_all_car):
        expected_message = 'No free car available'
        actual_message = car_api_service.get_car().get('message')
        assert actual_message == expected_message, f'Incorrect message when all car are absent:' \
            f'\n{actual_message} but must be\n{expected_message}'
