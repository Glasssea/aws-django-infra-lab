from django.urls import path
from . import views  # memorymaze 앱의 views를 import

app_name = 'memorymaze'

urlpatterns = [
    path('', views.index, name='index'),
    
]