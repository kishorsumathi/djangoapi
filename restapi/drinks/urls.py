from django.contrib import admin
from django.urls import path
from drinks.views import drink_list,send_file

urlpatterns = [
    path('', drink_list,name="drinks"),
    path("drinks/<path:filename>",send_file)
]
