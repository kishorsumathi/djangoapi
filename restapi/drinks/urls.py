from django.contrib import admin
from django.urls import path
from drinks.views import drink_list

urlpatterns = [
    path('', drink_list,name="drinks"),
]
