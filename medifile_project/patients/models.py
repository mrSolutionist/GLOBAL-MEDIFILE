from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user = get_user_model()


class PatientsData(models.Model):
    newPat = models.ForeignKey(user, on_delete=models.CASCADE)
    
    # detailForm = models.OneToOneField(user, on_delete=models.CASCADE)