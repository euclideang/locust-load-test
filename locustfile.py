import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    auth_url = "https://login.microsoftonline.com/ca4eb3f5-6926-47a6-b50d-054a4d36dfdd/oauth2/token"
    wait_time = between(5,10)
    access_token = None


    @task
    def powerautomate(self):
        result = self.client.post('https://smvs-dev.crm.dynamics.com/api/data/v9.1/msemr_appointmentemrs', json={
    "smvs_appointmentdatetime":"2021-01-02T08:45:00Z",
    "smvs_associatedclinicday": "90538093-d163-eb11-a812-0022481f8465",
    "smvs_associatedpatientid": "1ef7a561-ff61-eb11-a812-0022481e27b7"
}, headers=dict(authorization="Bearer {}".format(self.access_token)))
        print(result.text)

    def on_start(self):
        data = dict(
        grant_type="client_credentials",
    client_id="99448737-7541-491e-bd84-a4977799a66d",
    client_secret="19w2SlT41WRJy3.oYk27JM~k_rgy7n_r-Y",
    resource="https://smvs-dev.crm.dynamics.com/")
        response = self.client.post(self.auth_url,data=data)
        access_token = (response.json())["access_token"]
        self.access_token = access_token
