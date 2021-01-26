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
    def powerautomate(self):
        result = self.client.post('https://prod-78.westus.logic.azure.com:443/workflows/7bce6999af23483c911f589329d90906/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=6fV-EzDpwuXSeZ9i14aeoOOAZSHN40UHwnRbsB2jLkE')
