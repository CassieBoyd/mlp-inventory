import sqlite3
from django.shortcuts import render
from ponyapp.models import Pony


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

        new_pony = Pony.objects.create(
            price = form_data['price'],
            details = form_data['details']
        )

    return redirect(reverse('ponyapp:ponies'))