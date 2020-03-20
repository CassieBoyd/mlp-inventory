# My Little Pony Inventory
Have you ever looked at your extensive My Little Pony collection and thought "Wow, I think this is getting to the point where I should probably have my collection insured! But how do I accurately value and record them all?" We've all been there. My Little Pony Inventory endeavors to remedy this situation by creating a place for collectors to keep a record of their collection so they can quickly assess the total value of their ponies. 

(https://res.cloudinary.com/proplan/image/upload/v1584721701/MLPInventory/Screen_Shot_2020-03-19_at_11.03.43_AM_rxc3ns.png)

# Instructions for installing My Little Pony Inventory
- Clone this repo using the following command then cd into it

    `git clone git@github.com:CassieBoyd/mlp-inventory.git`

- For Mac users: create your OSX virtual environment in Terminal

    `python -m venv ponyenv`
    `source ./ponyenv/bin/activate`

- For Windows users: create your Windows virtual environment in Command Line

    `python -m venv workforceenv`
    `source ./workforceenv/Scripts/activate`

- Install the app's dependencies

    `pip install -r requirements.txt`

- Build your database from the existing models

    `python manage.py makemigrations ponyapp`
    `python manage.py migrate`

- Create a superuser for your local version of the app

    `python manage.py createsuperuser`

- Populate your database with initial data from fixtures files: (NOTE: every time you run this it will remove exisiting data and repopulate the tables)

    `python manage.py loaddata generation`
    `python manage.py loaddata bodystyle`
    `python manage.py loaddata country`
    `python manage.py loaddata condition`
    `python manage.py loaddata pony`
    `python manage.py loaddata userpony`

- Run your dev server

    `python manage.py runserver`

# Entity Relationship Diagram

(https://res.cloudinary.com/proplan/image/upload/v1584721922/MLPInventory/Screen_Shot_2020-03-20_at_11.31.16_AM_kn7abu.png)