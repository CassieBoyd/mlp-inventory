import sqlite3
from django.shortcuts import render, redirect, reverse
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
            condition_id = form_data['condition'],
            pony_id = form_data['pony'],
            user_id = request.user.id
        )

    return redirect(reverse('ponyapp:ponies'))