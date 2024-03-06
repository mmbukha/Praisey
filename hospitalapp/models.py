from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
          return self.name

class Member(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Appointment(models.Model):
       name = models.CharField(max_length=200)
       email = models.EmailField()
       phone_number = models.CharField(max_length=200)
       date = models.DateField()
       department = models.CharField(max_length=200)
       doctor = models.CharField(max_length=200)
       message = models.TextField()

       def __str__(self):
           return self.name



class ImageModel(models.Model):
   image = models.ImageField(upload_to='images/')
   title = models.CharField(max_length=50)
   price = models.IntegerField(null=True)