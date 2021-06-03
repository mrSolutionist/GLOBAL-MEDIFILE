from django.urls import path
from . import views
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def test(request):
    user = get_user_model()
    # x = user.objects.filter(doctorsdata__isnull=False)
    # print(x)
    hospital = user.objects.filter(request.user)
    print (hospital)
    return HttpResponse("test")
urlpatterns = [
    path('doc_signup', views.doctor_signup, name='doctor_signup'),
    path('hosp_signup', views.hospital_signup, name='hospital_signup'),
    path('pat_signup', views.patient_signup, name='patient_signup'),
    path('login', views.Newlogin, name='login'),
    path('news', views.news, name='news'),
    path('test/', test, name='news'),

    

]
