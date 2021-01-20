import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    base_url = 'https://smvs-dev.crm.dynamics.com/api/data/v9.1'
    api_url = 'https://svna-portal-api-dev.azurewebsites.net'
    auth_url = 'https://login.microsoftonline.com/ca4eb3f5-6926-47a6-b50d-054a4d36dfdd/oauth2/token'
    host = "https://smvs-dev.crm.dynamics.com"
    wait_time = between(5,10)
    access_token = None

    @task
    def clinic(self):
        result = self.client.get("/api/data/v9.1", headers=dict(authorization="Bearer {}".format(self.access_token)))

    @task
    def svna_clinics(self):
        result = self.client.get("{base_url}/svna_clinicses".format(base_url=self.base_url), headers=dict(authorization="Bearer {}".format(self.access_token)))

    @task
    def payer_list(self):
        result = self.client.get("{base_url}/svna_insuranceorganizations".format(base_url=self.base_url), headers=dict(authorization="Bearer {}".format(self.access_token)))

    def on_start(self):
        data = dict(grant_type="client_credentials", client_id='99448737-7541-491e-bd84-a4977799a66d',  client_secret='19w2SlT41WRJy3.oYk27JM~k_rgy7n_r-Y', resource='https://svnacovid.crm.dynamics.com/')
        response = self.client.post(self.auth_url,data=data)
        access_token = (response.json())["access_token"]
        self.access_token = access_token
