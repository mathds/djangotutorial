# djangotutorial

## Build a basic website with Django.

Tutorial link : https://tutorial.djangogirls.org/en/


## Virtual environnement

It isolate your Python/Django setup on a per-project basis,any changes you make to one website won't affect any others you're also developing.

* Create new virtual environnement

```python
python3 -m venv myvenv
```

* Activating the virtual environnement 

```python
myvenv\Scripts\activate
```

## Django project 

* Create a new Django project :

```python
django-admin.exe startproject mysite 
```

* Concerning the files in **mysite** : 
 ** *manage.py* is a script that helps with the management of the site
 ** *settings.py* is a file that contains the configuration of your website

* Create a database : 

```python
python manage.py migrate
```

* Starting the web server :

```python
python manage.py runserver
```

* Create a separate application inside our project :

```python
python manage.py startapp blog
```

Next step : add *app* into **settings.py > INSTALLED_APPS**

* Create models in **app/models.py** 

* Create new model in DB :

```python
python manage.py makemigrations blog
python manage.py migrate blog
```

To add, edit and delete the elements we've just modeled, we will use Django admin, in **app/admin.py**


* Create superuser :

```python
python manage.py createsuperuser
```

* URL management : redirect URL to views with regex

* **views/py** : where the logic is, request info from the model, pass it to a template, can do computing  


## 














