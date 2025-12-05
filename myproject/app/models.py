from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=25)
    desc=models.CharField(max_length=25)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

class Trashmodel(models.Model):
    title=models.CharField(max_length=25)
    desc=models.CharField(max_length=25)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
class Completemodel(models.Model):
    title=models.CharField(max_length=25)
    desc=models.CharField(max_length=25)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    