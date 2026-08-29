from django.urls import path
from . import views  # TRBT_main 앱의 views를 import

app_name = 'TRBT_main'

urlpatterns = [
    path('', views.index, name='index'),
    
]