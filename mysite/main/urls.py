from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="main"),
    path("test", views.main_page, name="main_page"),
    path("api", views.send_geo_data, name="send_geo_data"),
]