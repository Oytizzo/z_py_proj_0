# for User class
from locust import User, task


class NormalUser(User):

    @task
    def launch(self):
        print("Launching the task 1")

    @task
    def search(self):
        print("Starting")
