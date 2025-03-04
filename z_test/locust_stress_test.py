from locust import HttpUser, task, between, TaskSet

class RawDataEndpoint(TaskSet):
    @task
    def post_raw_data(self):
        self.client.post("/raw-data")

class DataEndpoint(TaskSet):
    @task
    def get_data(self):
        # Using a different client as this has a different base URL
        self.client.get("/data", name="/data")

class ApiUser(HttpUser):
    wait_time = between(4.5, 5.5)  # Around 5 seconds between tasks

    @task(1)
    def raw_data_tasks(self):
        # For the POST endpoint
        self.client.base_url = "http://localhost:8000"
        self.post_raw_data()

    @task(1)
    def data_tasks(self):
        # For the GET endpoint
        self.client.base_url = "http://0.0.0.0:8001"
        self.get_data()

    def post_raw_data(self):
        self.client.post("/raw-data")

    def get_data(self):
        self.client.get("/data")