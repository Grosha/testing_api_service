class API:
    URL = 'http://localhost:8000'

    def __int__(self):
        # self.URL = 'http://localhost:8000'
        # self.car_ = f'{API.URL}/car'
        self.delete_car = f'{API.URL}/car/'
        # self.car_list = f'{API.URL}/car_list'

    @staticmethod
    def car():
        return f'{API.URL}/car'

    @staticmethod
    def update_car_detail(model):
        return f'{API.URL}/car/{model}/update'

    @staticmethod
    def car_list():
        return f'{API.URL}/car_list'
