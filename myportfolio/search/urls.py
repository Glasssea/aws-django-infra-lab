from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name ='search'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:nickname>/', views.search, name='search')
]
