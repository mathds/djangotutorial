"""
 Django tutorial reminder
"""

#### commenter ctrl-K decommenter ctrl-Q

### Virtual environnement 

# cd C:/Users/nico/Documents/00_LBL/01_Tutorials/djangotutorial/djangogirls

## What is it : 

# # It isolate your Python/Django setup on a per-project basis. 
# # This means that any changes you make to one website won't affect any 
# # others you're also developing.

# # Create new virtual environnement

# python3 -m venv myvenv

# # Working with virtual environnement 

# myvenv\Scripts\activate




# # Create Django project (don't forget the point, means in this directory) 

# django-admin.exe startproject mysite .

# # manage.py is a script that helps with management of the site

# # settings.py file contains the configuration of your website. TO CHANGE

# # create a database : we need to be in the directory that contains the manage.py file
 
# python manage.py migrate

# # starting the web server : in the directory that contains the manage.py file

# python manage.py runserver

# # create a separate application inside our project 

# python manage.py startapp blog

# # then add blog into setting.py > INSTALLED_APPS

# # create models in app/models.py 

# # create new model in DB :

# python manage.py makemigrations blog
# python manage.py migrate blog

# # To add, edit and delete the posts we've just modeled, we will use Django admin.
# # In app/admin.py

# # create superuser :

# python manage.py createsuperuser


# URL management
# Redirect URL to views with regex

# views.py
# where the logic is, request info from the model, pass it to a template, can do computing  







###################################################


# # # Deploy with PythonAnywhere

# clone the repository by writing into the bash : 

# git clone https://github.com/<your-github-username>/my-first-blog.git

# work with a virtual environnement

# virtualenv --python=python3.6 myvenv
# source myvenv/bin/activate

# do everything as in local


# # Django ORM and QuerySets
# how Django connects to the database and stores data in it
# QuerySets allow you to read the data from the database, filter it and order it.

# # Django shell
# display
# python manage.py shell

# display object 
# from blog.models import Post
# Post.objects.all()

# create object
# from django.contrib.auth.models import User
# User.objects.all()
# me = User.objects.get(username='mathieu') # mathieu is superuser
# Post.objects.create(author=me, title='Sample title', text='Test')

# query filter
# Post.objects.filter(author=me)
# Post.objects.filter(title__contains='title')
# from django.utils import timezone
# Post.objects.filter(published_date__lte=timezone.now())

# post = Post.objects.get(title="Sample title")
# post.publish()

# # Ordering objects
# Post.objects.order_by('created_date')
# Post.objects.order_by('-created_date')

# # chaining querysets
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


# to print a variable in Django templates, we use double curly brackets
# {{ posts }}

# python code in html template :
# {% for post in posts %}
    # <div></div>
# {% endfor %}






# # # Git 

# # Initialize repository

# $ git init
# Initialized empty Git repository in ~/djangogirls/.git/
# $ git config --global user.name "Your Name"
# $ git config --global user.email you@example.com

# # check status 

# git status

# # add untracked files (point is current directory)

# git add --all .

# # commit all 

# git commit -m
# with comments
# git commit -m "Changed the HTML for the site."

# # hook up git repository to the website and push

# $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
# $ git push -u origin master

## gitignore
# *.pyc
# *~
# __pycache__
# myvenv
# db.sqlite3
# /static
# .DS_Store











