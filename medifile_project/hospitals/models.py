from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class HospitalData (models.Model):
    hospital = models.ForeignKey(user,on_delete=models.CASCADE)
    # doctor = models.ForeignKey(user,on_delete=models.CASCADE)

    class Meta:
        db_table = 'HospitalData'

    def __str__(self):
        return str(self.hospital.name)

    # @property
    def get_doctors(self):
        x=[i for i in user.objects.filter(is_doctor=True,whichHosp=self.pk)]
        print (x)
        return x