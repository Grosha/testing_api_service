import re

import pytest

from api_services.response_messages import ResponseMessages
from api_services.api_services import CarApiService


class TestGetCar:

    def test_get_car(self):
        car = CarApiService.get_car()
        assert re.match(r'\w+', car['name']) is not None, 'Incorrect parameter name in car'
        assert re.match(r'\w+', car['model']) is not None, 'Incorrect parameter model in car'
        assert re.match(r'\w+', car['type']) is not None, 'Incorrect parameter type in car'
        assert re.match(r'\d+', str(car['status'])) is not None, 'Incorrect parameter status in car'

    @pytest.mark.parametrize(
        'model_name, message',
        [
            ({'model': 'Accord'}, {'model': 'Accord', 'name': 'Honda', 'status': 1, 'type': 'Sedan'}),
            ({'model': 'No car'}, 'Car model No car is absent in the list'),
        ]
    )
    def test_get_car_by_model(self, model_name, message):
        expected_car_information = CarApiService.get_car(params=model_name)

        assert expected_car_information == message, f'Incorrect car information for model:' \
                                                    f'\n{expected_car_information}, must be\n{message}'

    @pytest.mark.parametrize(
        'parameter, message',
        [
            ({'name': 'Honda'}, ResponseMessages.INCORRECT_PARAMETER),
            ({'status': 1}, ResponseMessages.INCORRECT_PARAMETER),
            ({'type': 'Sedan'}, ResponseMessages.INCORRECT_PARAMETER),
            ({'test': 'test'}, ResponseMessages.INCORRECT_PARAMETER)
        ]
    )
    def test_get_car_by_any_parameters(self, parameter, message):
        expected_car_information = CarApiService.get_car(params=parameter)

        assert expected_car_information == message, f'Incorrect car information for model:' \
                                                    f'\n{expected_car_information}, must be\n{message}'

    @pytest.fixture(scope="function", autouse=False)
    def rent_all_car(self):
        car_list = CarApiService.get_car_list()
        car_status_available = {'status': 0}
        car_status_not_available = {'status': 1}

        for car in car_list:
            CarApiService.update_car(model=car.get('model'), params=car_status_available)
        yield
        for car in car_list:
            CarApiService.update_car(model=car.get('model'), params=car_status_not_available)

    def test_get_car_when_no_available(self, rent_all_car):
        actual_message = CarApiService.get_car()
        assert actual_message == ResponseMessages.NO_FREE_CAR_AVAILABLE, f'Incorrect message when all car are absent:' \
                                                                         f'\n{actual_message} but must be\n{ResponseMessages.NO_FREE_CAR_AVAILABLE}'

    def test_get_car_fail(self):
        car = CarApiService.get_car()
        assert re.match(r'\w+', car['model']) is not None, 'Incorrect parameter model in car'
        assert re.match(r'\w+', car['type']) is not None, 'Incorrect parameter type in car'
        assert re.match(r'\d+', str(car['status'])) is not None, 'Incorrect parameter status in car'
        assert re.match(r'\d+', car['name']) is not None, 'Incorrect parameter name in car'
