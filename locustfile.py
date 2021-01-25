import time
from locust import HttpUser, task, between

# class QuickstartUser(HttpUser):
    # base_url = 'https://smvs-dev.crm.dynamics.com/api/data/v9.1'
    # api_url = 'https://svna-portal-api-dev.azurewebsites.net'
    # auth_url = 'https://login.microsoftonline.com/ca4eb3f5-6926-47a6-b50d-054a4d36dfdd/oauth2/token'
    # host = "https://smvs-dev.crm.dynamics.com"
    # wait_time = between(5,10)
    # access_token = None

    # @task
    # def clinic(self):
        # result = self.client.get("/api/data/v9.1", headers=dict(authorization="Bearer {}".format(self.access_token)))

    # @task
    # def appointment(self):
        # result = self.client.post("/api/data/v9.1/msemr_locations", headers=dict(authorization="Bearer {}".format(self.access_token),), json=dict( smvs_locationstatus=153940000))

    # def on_start(self):
        # data = dict(grant_type="client_credentials", client_id='99448737-7541-491e-bd84-a4977799a66d',  client_secret='19w2SlT41WRJy3.oYk27JM~k_rgy7n_r-Y', resource='https://smvs-dev.crm.dynamics.com')
        # response = self.client.post(self.auth_url,data=data)
        # access_token = (response.json())["access_token"]
        # self.access_token = access_token
class QuickstartUser(HttpUser):
    base_url = 'https://smvs-dev.crm.dynamics.com/api/data/v9.1'
    api_url = 'https://svna-portal-api-dev.azurewebsites.net'
    auth_url = 'https://login.microsoftonline.com/ca4eb3f5-6926-47a6-b50d-054a4d36dfdd/oauth2/token'
    host = "https://smvs-dev.crm.dynamics.com"
    wait_time = between(5,10)
    access_token = None


    @task
    def powerautomate(self):
        result = self.client.post('https://prod-119.westus.logic.azure.com:443/workflows/cb585123557c4394aab35934bc4955f8/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=LjOk_G8cVQEFWgsK4gp_vv0ZQIrR5DbwjSDLHhK3ZOQ')

    # def on_start(self):
        # data = dict(grant_type="client_credentials", client_id='99448737-7541-491e-bd84-a4977799a66d',  client_secret='19w2SlT41WRJy3.oYk27JM~k_rgy7n_r-Y', resource='https://smvs-dev.crm.dynamics.com')
        # response = self.client.post(self.auth_url,data=data)
        # access_token = (response.json())["access_token"]
        # self.access_token = access_token
