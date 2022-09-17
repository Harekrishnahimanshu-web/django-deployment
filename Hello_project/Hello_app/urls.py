from django.contrib import admin
from django.urls import path
from Hello_app import views

urlpatterns = [
    path('', views.index, name='Hello_project'),
]