import re

import pytest

from settings.response_messages import ResponseMessages
from settings.services import car_api_service


class TestGetCar:

    def test_get_car(self):
        car = car_api_service.get_car().get('message')
        re.match('.+', car.get('name'))
        re.match('.+', car.get('model'))
        re.match('.+', car.get('type'))
        re.match(r'\\n\d+\\n', str(car.get('status')))

    @pytest.mark.parametrize(
        'model_name, message',
        [
            ('Accord', {'model': 'Accord', 'name': 'Honda', 'status': 1, 'type': 'Sedan'}),
            ('No car', 'Car model No car is absent in the list'),
            # ('', ResponseMessages.CAR_MODEL_WAS_NOT_WRITTEN),
            # (None, ResponseMessages.CAR_MODEL_WAS_NOT_WRITTEN),
        ]
    )
    def test_get_car_by_model(self, model_name, message):
        expected_car_information = car_api_service.get_car(model=model_name).get('message')
        # actual_car_information = {'model': 'Accord', 'name': 'Honda', 'status': 1, 'type': 'Sedan'}

        assert expected_car_information == message, f'Incorrect car information for model:' \
            f'\n{expected_car_information}, must be\n{message}'

    @pytest.mark.parametrize(
        'parameter, message',
        [
            ('name=Honda', ResponseMessages.NO_FREE_CAR_AVAILABLE),
            ('status=1', ResponseMessages.NO_FREE_CAR_AVAILABLE),
            ('type=Sedan', ResponseMessages.NO_FREE_CAR_AVAILABLE),
            ('test=test', ResponseMessages.NO_FREE_CAR_AVAILABLE)
        ]
    )
    def test_get_car_by_any_parameters(self, parameter, message):
        expected_car_information = car_api_service.get_car(any_parameters=parameter).get('message')

        assert expected_car_information == message, f'Incorrect car information for model:' \
            f'\n{expected_car_information}, must be\n{message}'

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

    def test_get_car_for_fail(self):
        car = car_api_service.get_car().get('message')
        assert re.match('\d+', car.get('name')) == True
        # re.match(r'\\n\d+\\n', car.get('name'))
        # re.match('.+', car.get('model'))
        # re.match('.+', car.get('type'))
        # re.match(r'\\n\d+\\n', str(car.get('status')))
