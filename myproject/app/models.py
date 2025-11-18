from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=25)
    desc=models.CharField(max_length=25)

class Trashmodel(models.Model):
    title=models.CharField(max_length=25)
    desc=models.CharField(max_length=25)

class Completemodel(models.Model):
    title=models.CharField(max_length=25)
    desc=models.CharField(max_length=25)
    