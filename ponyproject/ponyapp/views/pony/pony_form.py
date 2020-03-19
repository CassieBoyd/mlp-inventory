import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ponyapp.models import Pony, UserPony, Condition

def get_pony(pony_id):
    pony = Pony.objects.get(pk=pony_id)

    return pony

def get_user_pony(user_pony_id):
    user_pony = UserPony.objects.get(pk=user_pony_id)

    return user_pony

def get_conditions():
    conditions = Condition.objects.all()
    return conditions

@login_required
def pony_form(request, pony_id):
    if request.method == 'GET':
        pony = get_pony(pony_id)
        conditions = get_conditions()
        template = 'ponies/form.html'
        context = {
            'pony': pony,
            'conditions': conditions
        }

        return render(request, template, context)

@login_required
def user_pony_edit_form(request, user_pony_id):

    if request.method == 'GET':
        pony = get_user_pony(user_pony_id)
        conditions = get_conditions()
        
        template = 'user_ponies/form.html'
        context = {
            'user_pony': pony,
            'conditions': conditions
        }

        return render(request, template, context)