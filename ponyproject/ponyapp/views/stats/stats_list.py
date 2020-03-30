import sqlite3
from django.shortcuts import render
from ponyapp.models import UserPony
from django.db.models import Sum, Count

def total_value(request):
    if request.method == 'GET':

        total = UserPony.objects.filter(user__id=request.user.id).aggregate(sum=Sum('price'))['sum']
        ponies_owned = UserPony.objects.filter(user__id=request.user.id).count()

        template = 'stats/list.html'
        context = {
            'total': round(total,2),
            'ponies_owned' : ponies_owned
        }

        return render(request, template, context)