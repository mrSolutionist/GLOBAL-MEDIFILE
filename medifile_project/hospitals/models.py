from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class HospitalData (models.Model):
    hospital = models.ForeignKey(user,on_delete=models.CASCADE)