from django.urls import path
from .views import *

app_name = "ponyapp"

urlpatterns = [
    path('', pony_list, name='pony'),
    path('ponies/', pony_list, name='ponies'),
]