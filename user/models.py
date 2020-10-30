from django.db import models
from django.contrib.auth.models import User

# request libary is use to get couties API
import requests
# get method is use
res = requests.get('https://restcountries.eu/rest/v2/all')
# covert the response to json format
datas = res.json()

# request libary is use to get nigeria states API
res2 = requests.get('https://nigerian-states-info.herokuapp.com/api/v1/states')
datas2 = res2.json()


class UserData(models.Model):
    # use list comprenssion to loop through country list to give tuple of list
    NATIONALITY_CHOICES = [(data['name'][:14],data['name'][:14]) for data in datas[:240] ]
    GENDER_CHOICES = [('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')]
    STATES_CHOICES = [(state['Name'],state['Name'].upper()) for state in datas2['data']] 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=20, choices=NATIONALITY_CHOICES)
    state = models.CharField(max_length=30, choices=STATES_CHOICES, blank=True)

    def __str__(self):
         return f'{self.user.first_name} {self.user.last_name}'