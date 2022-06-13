# for User class
from locust import User, task, constant


class NormalUser(User):
    weight = 3
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the task 1")

    @task
    def search(self):
        print("Starting task 2")


class NormalUser2(User):
    weight = 3
    wait_time = constant(1)

    @task
    def launch2(self):
        print("Second Lanching the task 3")

    @task
    def search(self):
        print("Second Starting task 4")
