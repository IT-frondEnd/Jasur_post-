from tkinter.font import names

from django.urls import path
from .views import index


urlpatterns = [
    path('',index,name='index'),
]