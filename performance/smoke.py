import time
from random import randint

from locust import HttpUser, between, task


class Smoke(HttpUser):
    wait_time = between(1, 2)
    list_models = ['Accord', 'CLS200', 'Land Cruiser']

    @task
    def on_start(self):
        self.client.get("/ping")

    @task(5)
    def add_car(self):
        model = f'Accord v{randint(0, 1000)}'
        self.list_models.append(model)
        new_car = '{"name":"Honda", "model":"' + model + '", "type":"Sedan", "status":1}'
        self.client.post('/car', json=new_car)

    @task(4)
    def get_car(self):
        self.client.get('/car')

    @task
    def delete_car(self):
        model = self.list_models.pop()
        self.client.delete(f'/car/{model}')

    # @task(3)
    # def view_item(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    def get_car_list(self):
        self.client.get("/car_list")
        # self.client.post("/login", json={"username":"foo", "password":"bar"})
