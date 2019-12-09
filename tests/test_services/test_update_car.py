import json
from datetime import datetime

import pytest

from settings.response_messages import ResponseMessages
from settings.services import car_api_service


class TestUpdateCar:
    car = None
    date = None

    @pytest.fixture(scope="function", autouse=False)
    def add_new_car(self):
        self.date = datetime.now().strftime("%H:%M:%S")
        new_car = '{"name":"TestName", "model":"TestModel", "type":"TestType", "status":1}'
        self.car = json.loads(new_car)
        car_api_service.add_new_car(car=new_car).get('message')
        yield
        car_api_service.delete_car(model=self.car['model']).get('message')

    def test_update_car_name(self, add_new_car):
        new_car_name = f'{self.car["name"]}{str(self.date)}'
        update_car_response = car_api_service.update_car(model=self.car["model"], parameter=f'name={new_car_name}').get('message')
        actual_car_name = update_car_response['name']

        assert actual_car_name == new_car_name, f'Incorrect car name after it was updated: actual\n{actual_car_name} but must be\n{new_car_name}'

    def test_update_car_model(self, add_new_car):
        new_car_model = f'{self.car["model"]}{str(self.date)}'
        update_car_response = car_api_service.update_car(model=self.car["model"], parameter=f'model={new_car_model}').get('message')
        actual_car_model = update_car_response['model']

        assert actual_car_model == new_car_model, f'Incorrect car name after it was updated: actual\n{actual_car_model} but must be\n{new_car_model}'

    def test_update_car_type(self, add_new_car):
        new_car_type = f'{self.car["type"]}{str(self.date)}'
        update_car_response = car_api_service.update_car(model=self.car["model"], parameter=f'type={new_car_type}').get('message')
        actual_car_type = update_car_response['type']

        assert actual_car_type == new_car_type, f'Incorrect car name after it was updated: actual\n{actual_car_type} but must be\n{new_car_type}'

    def test_update_type_for_none_exist_car(self):
        update_car_response = car_api_service.update_car(model='test', parameter=f'type=test').get('message')

        assert update_car_response == ResponseMessages.CAR_ABSENT_IN_THE_LIST, 'Problem with update none exist cat in the list'

    @pytest.mark.parametrize(
        'parameter',
        [
            '',  # no parameters
            'test=test',  # none exist parameter
        ]
    )
    def test_update_car_negative(self, parameter, add_new_car):
        update_car_response = car_api_service.update_car(model=self.car["model"], parameter=parameter).get('message')

        assert update_car_response == self.car, 'Problem with negative cases'

