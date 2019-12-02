class API:
    URL = 'http://localhost:8000'

    def __int__(self):
        # self.URL = 'http://localhost:8000'
        self.car_ = f'{API.URL}/car'
        self.delete_car = f'{API.URL}/car/'
        self.car_list = f'{API.URL}/car_list'

    def car(self):
        return f'{API.URL}/car'
