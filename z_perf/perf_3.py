# for HttpUser class
from locust import HttpUser, task, between


class APIUser(HttpUser):
    host = "https://reqres.in"
    wait_time = between(1, 2)

    # @task
    def get_user(self):
        response = self.client.get("/api/users?page=2")
        print(response.status_code)
        print(response.headers)
        print(response.text)

    @task
    def create_user(self):
        response = self.client.get("/api/users", data="{'name': 'hello', 'job': 'world'}")
        print(response.status_code)
        print(response.headers)
        print(response.text)
