from django.urls import path

from . import views


app_name = "where_you_die"

urlpatterns = [
    path("", views.index, name="index"),
]
