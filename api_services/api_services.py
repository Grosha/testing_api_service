import logging

import requests


class BaseApiClient:

    @staticmethod
    def make_get(url, params=None, headers=None):
        response = requests.get(url, params, headers=headers)
        return ExtendedResponse(response).json()

    @staticmethod
    def make_post(url, headers=None, json_dict=None):
        response = requests.post(url, json=json_dict, headers=headers)
        return ExtendedResponse(response).json()

    @staticmethod
    def make_delete(url, headers=None):
        response = requests.delete(url, headers=headers)
        return ExtendedResponse(response).json()

    @staticmethod
    def make_patch(url, params=None, headers=None):
        response = requests.patch(url, params=params, headers=headers)
        return ExtendedResponse(response).json()


class ExtendedResponse:
    def __init__(self, response):
        logging.info(f"Request url {response.url} type {response.request.method}  body {response.request.body} ")
        self.res_json = None
        try:
            self.res_json = response.json()
        except Exception:
            pass
        logging.info(f"Response status code {response.status_code} body {self.res_json}")

        # self.inner_response = response

    # def assert_status_code(self, status_code):
    #     try:
    #         json = self.inner_response.json()
    #     except JSONDecodeError:
    #         json = ''
    #     assert self.inner_response.status_code == status_code, \
    #         f'Status code mismatch. expected: {status_code} actual: {self.inner_response.status_code}\n{json}'
    #     return self

    def json(self):
        return self.res_json


class APICalls:
    BASE_URL = 'http://localhost:8000'

    @staticmethod
    def ping() -> str:
        return f'{APICalls.BASE_URL}/ping'

    @staticmethod
    def car() -> str:
        return f'{APICalls.BASE_URL}/car'

    @staticmethod
    def car_list() -> str:
        return f'{APICalls.BASE_URL}/car_list'

    @staticmethod
    def update_car_info(model) -> str:
        return f'{APICalls.BASE_URL}/car/update/{model}'

    @staticmethod
    def delete_car(model) -> str:
        return f'{APICalls.BASE_URL}/car/{model}'


class CarApiService:

    @staticmethod
    def get_car(params=None):
        return BaseApiClient.make_get(APICalls.car(), params).get('message')

    @staticmethod
    def get_car_list():
        return BaseApiClient.make_get(APICalls.car_list()).get('message')

    @staticmethod
    def ping():
        return BaseApiClient.make_get(APICalls.ping())

    @staticmethod
    def add_new_car(car=None):
        return BaseApiClient.make_post(APICalls.car(), json_dict=car).get('message')

    @staticmethod
    def delete_car(model):
        return BaseApiClient.make_delete(APICalls.delete_car(model)).get('message')

    @staticmethod
    def update_car(model, params=None):
        return BaseApiClient.make_patch(APICalls.update_car_info(model), params=params).get('message')
