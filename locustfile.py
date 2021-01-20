import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    host = "https://svnacovid.crm.dynamics.com"
    auth_url  = "https://login.microsoftonline.com/8f4472fe-3110-4c60-b364-ffe3873b1295/oauth2/token"
    wait_time = between(5,10)

    access_token = None

    @task
    def hello_world(self):
        result = self.client.get("/api/data/v9.1", headers=dict(authorization="Bearer {}".format(self.access_token)))

    def on_start(self):
        data = dict(grant_type="client_credentials", client_id='6af28d02-3925-4fee-a6b5-97b70cfda92b',  client_secret='HK8BdN_51sM_.dHX2y_tC-Q0Ltvayg6t01', resource='https://svnacovid.crm.dynamics.com/')
        response = self.client.post(self.auth_url,data=data)
        access_token = (response.json())["access_token"]
        self.access_token = access_token
