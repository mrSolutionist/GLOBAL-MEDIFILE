from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()


class DoctorsData(models.Model):
    newDoc = models.ForeignKey(user,on_delete=models.CASCADE)
