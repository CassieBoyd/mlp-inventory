import sqlite3
from django.shortcuts import render
from ponyapp.models import UserPony
from django.db.models import Sum

def total_value(request):
    if request.method == 'GET':

        total = UserPony.objects.aggregate(sum=Sum('price'))['sum']

        template = 'stats/list.html'
        context = {
            'total': round(total,2)
        }

        return render(request, template, context)