import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    url  = "http://google.com"
    @task
    def hello_world(self):
        self.client.get(self.url)
        self.client.get(self.url)

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(self.url)
            time.sleep(1)

    def on_start(self):
        self.client.post(self.url, json={"username":"foo", "password":"bar"})
