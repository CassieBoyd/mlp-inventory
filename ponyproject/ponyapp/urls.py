from django.urls import path
from .views import *

app_name = "ponyapp"

urlpatterns = [
    path('', home, name='home'),
    path('ponies/', pony_list, name='ponies'),
]