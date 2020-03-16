import sqlite3
from django.shortcuts import render
from ponyapp.models import Pony, UserPony


def pony_list(request):
    if request.method == 'GET':
        all_ponies = Pony.objects.all()
        template = 'ponies/list.html'
        context = {
            'all_ponies': all_ponies
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_pony = UserPony.objects.create(
            price = form_data['price'],
            details = form_data['details'],
            condition = form_data['condition']
        )

    return redirect(reverse('ponyapp:ponies'))