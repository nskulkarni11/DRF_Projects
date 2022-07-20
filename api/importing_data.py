import requests
import json
from .models import MyUser
from django.core.management.base import BaseCommand


IMPORT_URL = 'https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json'

class command(BaseCommand):
    def import_user(self,data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        company_name = data.get('company_name')
        age = data.get('age')
        city = data.get('city')
        state = data.get('state')
        zip = data.get('zip')
        email = data.get('email')
        web = data.get('web')
        try:
            user,created = MyUser.objects.get_or_create(
                first_name = first_name,
                last_name = last_name,
                company_name = company_name,
                age = age,
                city = city,
                state = state,
                zip = zip,
                email = email,
                web = web
            )
            if created:
                MyUser.save()
        except Exception as ex:
            print('Failed')
    def handle(self,*args, **options):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=IMPORT_URL,headers=headers,)
        response.raise_for_status()
        data = response.json()
        for data_object in data:
            self.import_user(data_object)