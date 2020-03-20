import sqlite3
from django.shortcuts import render
from ponyapp.models import UserPony

def total_value(request):
    if request.method == 'GET':
        
        all_prices = UserPony.objects.count()
        print("All Prices:", all_prices)

        template = 'stats/list.html'
        context = {
            'all_prices': all_prices
        }

        return render(request, template, context)