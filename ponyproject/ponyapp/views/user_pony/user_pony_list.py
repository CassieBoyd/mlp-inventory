import sqlite3
from django.shortcuts import render
from ponyapp.models import UserPony


def user_pony_list(request):
    if request.method == 'GET':
        all_ponies = UserPony.objects.all()
        template = 'user_ponies/list.html'
        context = {
            'all_ponies': all_ponies
        }

        return render(request, template, context)

