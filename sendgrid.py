import time
import datetime
import math
from locust import HttpUser, task, between
import random

slot_start_time = datetime.datetime(year=2021, month=2, day=1, hour = 2, minute=15)
def slots(start_time, duration, shot_duration):
    slots_ = math.floor(duration/shot_duration)
    result = [start_time]
    current = start_time

    for _  in range(1, slots_):
        next_ = current + datetime.timedelta(minutes=shot_duration)
        result.append(next_)
        current = next_

    return result



available_slots = slots(slot_start_time, 540, 15)

def format_datetime(_date):
    return _date.strftime("%Y-%m-%dT%H:%M:00Z")

class QuickstartUser(HttpUser):

    auth_url = 'https://login.microsoftonline.com/4ec8fabd-a127-4740-8cd2-0a056e1bf24b/oauth2/token'
    wait_time = between(5,10)
    access_token = None



    @task
    def clinics(self):
        # result = self.client.get('https://mvs-uat.crm.dynamics.com/api/data/v9.1/smvs_appointment_slot_availabilities')
        # result = self.client.get('https://mvs-patientportal-uat-api.azurewebsites.net/api/clinicdays/clinics/8dc5613f-8465-eb11-a812-0022481e5310')
        # ?$filter=_mvs_locationid_value eq cb0602c6-5165-eb11-a812-0022481f8465
        result = self.client.post('https://prod-92.westus.logic.azure.com:443/workflows/0719be614d9a48eb8a1e3937a0f0ea2f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=9dUQV_7_5Te5qh8Z8h2W2UnUDPokHkRdIYdXJ4VICIs')
        # print(result.text)
    # @task
    # def powerautomate(self):
        # slot = random.choice(available_slots)
        # _datetime = format_datetime(slot)
        # result = self.client.post('https://mvs-uat.crm.dynamics.com/api/data/v9.1/msemr_appointmentemrs', json={
    # "smvs_appointmentdatetime": _datetime,
    # "smvs_associatedclinicday": "8bad4cef-9a64-eb11-a812-0022481e5ae1",
    # "smvs_associatedpatientid": "f7140e86-5162-eb11-a812-0022481e21b9"
# }, headers=dict(authorization="Bearer {}".format(self.access_token)))
        # print(result.text)


    # def on_start(self):
        # data = dict(
        # grant_type="client_credentials",
    # client_id="2b407b99-6fb3-4921-ae96-e7126bba674b",
    # client_secret="EGVF82epqfJ__3.08nZS1ld~3NvAEYsOf-",
    # resource="https://mvs-uat.crm.dynamics.com/")
        # response = self.client.post(self.auth_url,data=data)
        # access_token = (response.json())["access_token"]
        # self.access_token = access_token
        # # print(self.access_token)
