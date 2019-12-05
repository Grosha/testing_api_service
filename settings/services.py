import json

from apiclient import APIClient


class BaseApiClient(APIClient):

    def _compose_url(self, path):
        return self.BASE_URL + path

    def _handle_response(self, response):
        return json.loads(response.data)

    def _request(self, method, path, headers=None, body=None):
        url = self._compose_url(path)

        self.rate_limit_lock and self.rate_limit_lock.acquire()
        r = self.connection_pool.urlopen(method.upper(), url, headers=headers, body=body)

        return self._handle_response(r)

    def make_get(self, path, headers=None):
        return self._request('GET', path, headers)

    def make_post(self, path, headers=None, body=None):
        return self._request('POST', path, headers, body)

    def make_delete(self, path, headers=None):
        return self._request('DELETE', path, headers)

    def make_patch(self, path, headers=None):
        return self._request('PATCH', path, headers)


class CarApiService(BaseApiClient):
    BASE_URL = 'http://localhost:8000'

    def get_car(self, model=None):
        if model:
            return self.make_get(f'/car?model={model}')
        else:
            return self.make_get('/car')

    def get_car_list(self):
        return self.make_get('/car_list')

    def add_new_car(self, headers='Content-Type: application/json', body=None):
        return self.make_post(f'/car', headers=headers, body=body)

    def delete_car(self, model):
        return self.make_delete(f'/car/{model}')

    def update_car(self, model, parameter):
        return self.make_patch(f'/car/update/{model}?{parameter}')


car_api_service = CarApiService()
