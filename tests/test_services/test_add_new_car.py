import json
from random import randint

import pytest

from api_services.rent_car_company import CarType, CarStatus, Car
from api_services.response_messages import ResponseMessages
from api_services.api_services import CarApiService


class TestAddNewCar:

    def test_add_new_car(self):
        model = f'Accord v{randint(0, 1000)}'
        # new_car = '{"name":"Honda", "model":"' + model + '", "type":"Sedan", "status":1}'
        new_car = Car('Honda', model, CarType.SEDAN, CarStatus.AVAILABLE).get_car_info()
        add_response_message = CarApiService.add_new_car(car=new_car)

        assert add_response_message == ResponseMessages.NEW_CAR_ADDED, f'Problem with adding car:' \
                                                                       f'\n{add_response_message}, must be\n{ResponseMessages.NEW_CAR_ADDED}'

    def test_add_presented_car(self):
        new_car = '{"name":"Honda", "model":"Accord", "type":"Sedan", "status":1}'
        add_response_message = CarApiService.add_new_car(car=new_car)

        assert 'Car presence in the list:' in add_response_message, f'Problem with adding presented car:' \
                                                                    f'\n{add_response_message}'

    @pytest.mark.parametrize(
        'new_car, message',
        [
            ('{}', "Incorrect parameter 'model' in json body for object Car"),
            ('{"sd":"Accord", "model":"Hondas", "type":"Sedan", "status":1}',
             "Incorrect parameter 'name' in json body for object Car"),
            ('{"name":"Accord", "models":"Hondas", "type":"Sedan", "status":1}',
             "Incorrect parameter 'model' in json body for object Car"),
            ('{"name":"Accord", "model":"Hondas"}', "Incorrect parameter 'type' in json body for object Car"),
            ('{"name":"Accord", "model":"Hondas", "type":"Sedan", "statas":1}',
             "Incorrect parameter 'status' in json body for object Car"),
            ('{"name":"Accord", "model":"Hondas", "type":"Sedan"}',
             "Incorrect parameter 'status' in json body for object Car"),
            ('', 'Problem with json the JSON object must be str, bytes or bytearray, not NoneType'),
        ]
    )
    def test_negative_cases(self, new_car, message):
        # new_car = '{"name":"Accord", "model":"Honda", "type":"Sedan", "status":1}'
        add_response_message = CarApiService.add_new_car(car=new_car)

        assert message == add_response_message, 'Incorrect error while server was adding new car'

    def test_smoke_suite(self):
        new_car = f'{"name":"Lamborghini", "model":"Huracan{randint(0, 1000)}", "type":"sportcar", "status":1}'

        # add new car
        add_response_message = CarApiService.add_new_car(car=new_car)
        add_message = 'New car added'
        assert add_response_message == add_message, f'Problem with adding car:' \
                                                    f'\n{add_response_message}, must be\n{add_message}'

        # get just added car
        new_car = json.loads(new_car)
        model_parameter = {'model': new_car['model']}
        new_car_information = CarApiService.get_car(params=model_parameter)
        assert new_car_information == new_car, f'Incorrect car information for model:' \
                                               f'\n{new_car_information}, must be\n{new_car}'

        # update car
        new_model = f'Test{new_car["model"]}'
        new_model_parameter = {'model': new_model}
        update_car_response = CarApiService.update_car(model=new_car["model"], params=new_model_parameter)
        assert update_car_response['model'] == new_model, f'Incorrect car information for model after update:' \
                                                          f'\n{update_car_response}, must be\n{new_model}'

        # remove just added/updated car
        delete_response_message = CarApiService.delete_car(model=new_model)
        delete_message = f'Car model {new_model} removed'
        assert delete_response_message == delete_message, f'Problem with delete car:' \
                                                          f'\n{delete_response_message}, must be\n{delete_message}'

        # get removed car
        no_car_response = CarApiService.get_car(params=new_model_parameter)
        no_car_message = f'Car model {new_model} is absent in the list'
        assert no_car_response == no_car_message, f'Removed car presence in the list:' \
                                                  f'\n{no_car_response}, must be\n{no_car_message}'
