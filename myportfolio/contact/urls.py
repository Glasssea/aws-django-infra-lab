from django.urls import path
from . import views  # main 앱의 views를 import

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]