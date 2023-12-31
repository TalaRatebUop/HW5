from django.db import models

# Create your models here.
class ClientType(models.Model):
    type=models.IntegerField(primary_key=True,default=0)
    name=models.CharField(max_length=20)
    description=models.CharField(null=False,max_length=25)
    def __str__(self):
        return self.name
class Client(models.Model):
    cid=models.AutoField(primary_key=True,default=0)
    name=models.CharField(max_length=20)
    gender_ch=[(1,"Female"),(2,"Male")]
    gender=models.IntegerField(choices=gender_ch)
    email=models.EmailField(null=True, unique=True)
    birthdate=models.DateField()
    type=models.ForeignKey(ClientType,on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.name

class Product(models.Model):
    Pid=models.IntegerField(primary_key=True,default=0)
    name=models.CharField(max_length=20)
    description=models.CharField(null=False,max_length=20)
    def __str__(self):
        return self.name
class Order(models.Model):
    Oid=models.IntegerField(primary_key=True,default=0)
    Pid=models.ForeignKey(Product,on_delete=models.CASCADE,default=0)
    cid = models.ForeignKey(Client,on_delete=models.CASCADE,default=0)
    OrderDate = models.DateField()
    ShippingDate = models.DateField()
    def __int__(self):
        return self.Oid






