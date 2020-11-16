from locust import HttpUser, between, task


class RentCarUser(HttpUser):
    weight = 1
    wait_time = between(1, 2)

    @task
    def on_start(self):
        self.client.get("/ping")

    @task
    def get_car(self):
        self.client.get('/car')

    @task(4)
    def get_car_list(self):
        self.client.get("/car_list")
