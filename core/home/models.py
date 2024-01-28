from django.db import models

# Create your models here.
# we create our database models here for this app

# Let's create Student Model



# Structure of a model
class Student(models.Model):
    # id = models.AutoField()   # This is automatically added by django which is primary key 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True)
    file = models.FileField()
 
class Product(models.Model):
    pass