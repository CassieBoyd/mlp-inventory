import sqlite3
from django.shortcuts import render
from ponyapp.models import UserPony
from django.db.models import Sum

def total_value(request):
    if request.method == 'GET':
        
        total = UserPony.objects.aggregate(sum=Sum('price'))['sum']
        print("All Prices:", total)

        template = 'stats/list.html'
        context = {
            'total': total
        }

        return render(request, template, context)