from django.db import models

# Create your models here.

class Customer(models.Model):
    Ac_num = models.BigIntegerField(unique=True)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField(null=True)
    Email_id = models.EmailField()
    Ph_number = models.BigIntegerField(unique=True)
    Balance = models.BigIntegerField(default=0)
   

class User_Statements(models.Model):
    User = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Statement')
    Amount = models.IntegerField()
    History = models.CharField(max_length=50)
    Date = models.DateField(auto_now_add=True)

    
