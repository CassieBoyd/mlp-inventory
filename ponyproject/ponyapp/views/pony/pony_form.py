import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ponyapp.models import Pony, UserPony

def get_pony(pony_id):
    pony = Pony.objects.get(pk=pony_id)

    return pony

@login_required
def pony_form(request, pony_id):
    if request.method == 'GET':
        pony = get_pony(pony_id)
        template = 'ponies/form.html'
        context = {
            'pony': pony
        }

        return render(request, template, context)

@login_required
def pony_edit_form(request, pony_id):

    if request.method == 'GET':
        pony = get_pony(pony_id)
        ponies = get_ponies()

        template = 'ponies/form.html'
        context = {
            'pony': pony,
            'all_ponies': ponies
        }

        return render(request, template, context)