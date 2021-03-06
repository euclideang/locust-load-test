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
    def get_slots(self):
        result  = self.client.get('https://smvs-patient-portal-api-dev.azurewebsites.net/api/health')
        print(result)

    # @task
    # def powerautomate(self):
        # result = self.client.post('https://prod-04.westus.logic.azure.com/workflows/a6265896ed994fceb655f23fce57c6ee/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=fIir5BfnZWm8ZbY_QwdAzm0QbHIvnOJjFym612OhAUM')
    # @task
    # def appointment(self):
        # result = self.client.post("/api/data/v9.1/msemr_locations", headers=dict(authorization="Bearer {}".format(self.access_token),), json=dict( smvs_locationstatus=153940000))

    # def on_start(self):
        # data = dict(grant_type="client_credentials", client_id='99448737-7541-491e-bd84-a4977799a66d',  client_secret='19w2SlT41WRJy3.oYk27JM~k_rgy7n_r-Y', resource='https://smvs-dev.crm.dynamics.com')
        # response = self.client.post(self.auth_url,data=data)
        # access_token = (response.json())["access_token"]
        # self.access_token = access_token
