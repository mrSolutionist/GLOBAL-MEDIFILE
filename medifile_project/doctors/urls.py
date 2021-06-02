from django.urls import path
from  .views import  doctorsIndex

urlpatterns=[
    path('',doctorsIndex,name='doctorsIndex')
]