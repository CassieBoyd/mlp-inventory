from django.urls import path
from .views import *
from django.urls import path

app_name = "ponyapp"

urlpatterns = [
    path('', home, name='home'),
    path('ponies/', pony_list, name='ponies'),
    path('ponies/<int:pony_id>/', pony_details, name='pony'),
]