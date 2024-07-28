from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="main"),
    path("test", views.main_page, name="main_page"),
    path("api/", views.get_active, name="get_data"),
    path("aid/", views.get_relocation, name="get_relocation"),
]