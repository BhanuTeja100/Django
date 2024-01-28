# <a href="https://github.com/BhanuTeja100/Django">Learning Django</a>
## Basic Setup
- Download Python from [Python](https://www.python.org/downloads/)
- Setting Up Virtual Environment

  ```
  pip install virtualenv
  ```
```
virtualenv env
```
- This will create a virtual environment with name env
- Then do cd env/Scripts/activate
- To activate the virtual environment
- Now you will get into the virtual environment which will be show as

  ![image](https://github.com/BhanuTeja100/Django/assets/88223893/1ca3f7df-f25a-4cc0-97ca-7ed4ea12c3f5)

- Now get back to the main path by doing cd .. two times


## Install Django
```
pip install Django
```
- This will install Django into your virtual environment


## Starting the Project

- You can create a new Django Project using
```
django-admin startproject core
```
- This command will create a project in the virtual environment with name core
- You can change the name of the project as you required
- Now do cd core

## Run Server 

- Run Server using the command
```
python manage.py runserver
```

- You can create app in the project based on your requirements using the command
```
python manage.py startapp myApp
```
- This will create a app with name myApp you can change this name

## Creating Models (Schema's in Sql)
- One can create models in the app in models.py
- Then you have to make migrations to make changes inside the database (sqlite here)
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- These commands are used to make changes in db
- You can refer these documents [Link](https://docs.djangoproject.com/en/5.0/topics/db/models/) for more information
