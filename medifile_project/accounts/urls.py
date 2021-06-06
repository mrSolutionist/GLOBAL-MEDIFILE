from django.urls import path
from . import views
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import  LogoutView

def test(request):
    user = get_user_model()
    # x = user.objects.filter(doctorsdata__isnull=False)
    # print(x)
    # hospital = user.objects.get(id=request.user.whichHosp)
    # print (hospital)

    # print(user.name,'/n',user.is_hospital,'/n',user.is_doctor)

    return HttpResponse("test")
urlpatterns = [
    path('doc_signup', views.doctor_signup, name='doctor_signup'),
    path('hosp_signup', views.hospital_signup, name='hospital_signup'),
    path('pat_signup', views.patient_signup, name='patient_signup'),
    path('login', views.Newlogin, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('news', views.news, name='news'),
    path('test/', test, name='news'),

    

]
