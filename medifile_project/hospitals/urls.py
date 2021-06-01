from django.urls import  path
from .views import hospitalIndex
urlpatterns = [
    path('',hospitalIndex,name='hospitalIndex')
]