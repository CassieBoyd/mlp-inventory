import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from ponyapp.models import UserPony


def get_pony(user_pony_id):
    return UserPony.objects.get(pk=user_pony_id)

# @login_required
def user_pony_details(request, user_pony_id):
    print("This is NOT a GET")
    if request.method == 'GET':
        print("This is a GET")

        user_pony = get_pony(user_pony_id)

        template = 'user_ponies/detail.html'
        context = {
            'user_pony': user_pony
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        # Check if this POST is for editing a pony
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            print("this is a print")
            # # retrieve it first:
            user_pony_to_update = UserPony.objects.get(pk=user_pony_id)

            # # Reassign a property's value
            # user_pony_to_update.pony_id = form_data['pony_id']
            user_pony_to_update.price = form_data['price']
            user_pony_to_update.details = form_data['details']
            user_pony_to_update.condition_id = form_data['condition']

            # # Save the change to the db
            user_pony_to_update.save()

            return redirect(reverse('ponyapp:user_pony_list'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            user_pony = UserPony.objects.get(pk=user_pony_id)
            user_pony.delete()

            return redirect(reverse('ponyapp:user_pony_list'))