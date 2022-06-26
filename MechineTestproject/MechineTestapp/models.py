from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class freg(models.Model):
    username = models.CharField(max_length=200,null=True,blank=False) 
    password =models.CharField(max_length=200,null=True,blank=False)
    repassword =models.CharField(max_length=200,null=True,blank=False)  
    email = models.CharField(max_length=200,null=True,blank=False)


class Creg(models.Model):
    userid = models.ForeignKey(freg,on_delete=CASCADE,null=True,blank=False)
    Fname = models.CharField(max_length=200,null=True,blank=False) 
    Lname = models.CharField(max_length=200,null=True,blank=False) 
    Relationship = models.CharField(max_length=200,null=True,blank=False) 
    gender = models.CharField(max_length=200,null=True,blank=False)  
    location = models.CharField(max_length=200,null=True,blank=False) 
    number = models.IntegerField(null=True,blank=False) 
    adrs = models.CharField(max_length=200,null=True,blank=False)
    img = models.ImageField(upload_to='image',null=True,blank=False) 

   