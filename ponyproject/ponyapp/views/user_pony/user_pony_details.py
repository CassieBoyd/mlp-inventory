import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from ponyapp.models import UserPony


def get_pony(user_pony_id):
    return UserPony.objects.get(pk=user_pony_id)

# @login_required
def user_pony_details(request, user_pony_id):
    if request.method == 'GET':
        user_pony = get_pony(user_pony_id)

        template = 'user_ponies/detail.html'
        context = {
            'user_pony': user_pony
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
    ):
        user_pony = UserPony.objects.get(pk=user_pony_id)
        user_pony.delete()

        return redirect(reverse('ponyapp:user_pony_list'))