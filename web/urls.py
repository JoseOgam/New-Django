from django.urls import path
from web import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]