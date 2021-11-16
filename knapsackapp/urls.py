from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
        path(r'', views.index, name='index'),
        path(r'aboutus', views.aboutus, name='aboutus'),
        path(r'input', views.input, name='input'),
        path(r'results', views.results, name='results'),
]
