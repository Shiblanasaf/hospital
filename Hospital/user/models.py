from django.db import models

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()


class Doctor(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    dept=models.CharField(max_length=100)

class Medicine(models.Model):
    mname=models.CharField(max_length=100,verbose_name='name')
    price=models.IntegerField()
    expiry=models.DateField()
    pharma_company=models.CharField(max_length=100)
    medicine_image=models.ImageField(upload_to="medicine_image",null=True)


class Staff(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    designation=models.CharField(max_length=100)




