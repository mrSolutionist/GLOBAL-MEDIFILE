from django.urls import path
from . import views


urlpatterns = [
    path('doc_signup', views.doctor_signup, name='doctor_signup'),
    path('hosp_signup', views.hospital_signup, name='hospital_signup'),
    path('login', views.Newlogin, name='login'),
    

]
