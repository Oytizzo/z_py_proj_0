from locust import HttpUser, task, between, User


class websiteuser(HttpUser):
    host = "https://google.com"
    wait_time = between(5, 10)

    @task
    def visit_homepage(self):
        # response = self.client.get("/api/users", data="{'name': 'hello', 'job': 'world'}")
        self.client.post("/submit/form", data="")

class anotheruser(user):
    host = "https://twitter.com"
    wait_time = between(5, 10)

