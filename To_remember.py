"""
 Django tutorial reminder
"""


## Virtual environnement 

# cd C:/Users/nico/Documents/00_LBL/01_Tutorials/djangotutorial

# What is it : 

# It isolate your Python/Django setup on a per-project basis. 
# This means that any changes you make to one website won't affect any 
# others you're also developing.

# Create new virtual environnement

# python3 -m venv myvenv

# Working with virtual environnement 

# myvenv\Scripts\activate




## Create Django project (don't forget the point, means in this directory) 

# django-admin.exe startproject mysite .

# manage.py is a script that helps with management of the site

# settings.py file contains the configuration of your website. TO CHANGE

# create a database : we need to be in the directory that contains the manage.py file
 
# python manage.py migrate

# starting the web server : in the directory that contains the manage.py file

# python manage.py runserver

# create a separate application inside our project 

# python manage.py startapp blog

# then add blog into setting.py > INSTALLED_APPS

# create models in app/models.py 

# create new model in DB :

# python manage.py makemigrations blog
# python manage.py migrate blog

# To add, edit and delete the posts we've just modeled, we will use Django admin.
# In app/admin.py

# create superuser :

# python manage.py createsuperuser












