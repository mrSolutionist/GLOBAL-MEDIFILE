from django.urls import path

from .views import conditionDetail

urlpatterns = [path('', conditionDetail, name='patDetail'),]
