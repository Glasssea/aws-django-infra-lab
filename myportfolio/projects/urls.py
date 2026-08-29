from django.urls import path
from . import views  # skillset 앱의 views를 import

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
 
]