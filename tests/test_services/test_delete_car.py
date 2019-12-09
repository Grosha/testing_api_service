from settings.response_messages import ResponseMessages
from settings.services import car_api_service


class TestDeleteCar:

    def test_delete_no_exist_car(self):
        delete_response_message = car_api_service.delete_car(model='RX350-').get('message')
        assert delete_response_message == ResponseMessages.CAR_ABSENT_IN_THE_LIST, f'Problem with delete car:' \
            f'\n{delete_response_message}, must be\n{ResponseMessages.CAR_ABSENT_IN_THE_LIST}'
