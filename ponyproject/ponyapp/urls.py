from django.urls import path, include
from .views import *

app_name = "ponyapp"

urlpatterns = [
    path('', home, name='home'),
    path('ponies/', pony_list, name='ponies'),
    path('ponies/<int:pony_id>/', pony_details, name='pony'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name='logout'),
    path('ponies/<int:pony_id>/form', pony_form, name='pony_form'),
    path('user_ponies/', user_pony_list, name='user_pony_list'),
    path('user_ponies/<int:user_pony_id>/', user_pony_details, name='user_pony'),
    path('user_ponies/<int:user_pony_id>/form/', user_pony_edit_form, name='user_pony_edit_form'),
    path('stats/', total_value, name='stats'),
]