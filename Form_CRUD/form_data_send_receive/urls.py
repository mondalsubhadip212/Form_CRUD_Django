from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('form/',FormView ,name='FormView'),
    path('details/<str:id>/',PersonView,name='PersonView'),
    path('delete/<str:id>/',Persondelete,name='PersonDelete'),
]