
from settings.services import car_api_service


class TestAddNewCar:

    def test_smoke_suite(self):
        new_car = '{"name":"Lamborghini", "model":"Huracan", "type":"sportcar", "status":1}'
        model = 'Huracan'

        add_response_message = car_api_service.add_new_car(body=new_car).get('message')
        add_message = f'Car model {model} removed'
        assert 1 == 'New car added', f'Problem with adding car:' \
            f'\n{add_response_message}, must be\n{add_message}'

        new_car_information = car_api_service.get_car(model=model).get('message')
        assert new_car_information == new_car, f'Incorrect car information for model:' \
            f'\n{new_car_information}, must be\n{new_car}'

        delete_response_message = car_api_service.delete_car(model=model).get('message')
        delete_message = f'Car model {model} removed'
        assert delete_response_message == delete_message, f'Problem with delete car:' \
            f'\n{delete_response_message}, must be\n{delete_message}'

        no_car_response = car_api_service.get_car(model=model).get('message')
        no_car_message = f'Car model {model} is absent in the list'
        assert no_car_response == no_car_message, f'Removed car presence in the list:' \
            f'\n{new_car_information}, must be\n{no_car_message}'
