import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from ponyapp.models import Pony


def get_pony(pony_id):
    return Pony.objects.get(pk=pony_id)

# @login_required
def pony_details(request, pony_id):
    if request.method == 'GET':
        pony = get_pony(pony_id)

        template = 'ponies/detail.html'
        context = {
            'pony': pony
        }

        return render(request, template, context)