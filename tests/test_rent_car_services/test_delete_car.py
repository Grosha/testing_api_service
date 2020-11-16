from api_services.response_messages import ResponseMessages
from api_services.api_services import CarApiService


class TestDeleteCar:

    def test_delete_no_exist_car(self):
        delete_response_message = CarApiService.delete_car(model='RX350-')\
            .assert_status_code(200)\
            .get_message()
        assert delete_response_message == ResponseMessages.CAR_ABSENT_IN_THE_LIST, f'Problem with delete car:' \
            f'\n{delete_response_message}, must be\n{ResponseMessages.CAR_ABSENT_IN_THE_LIST}'
