from uuid import uuid4

from django.db import models


class Employees(models.Model):
    id = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Offers(models.Model):
    id = models.AutoField(primary_key=True)
    medicament = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    status = models.IntegerField(default=0)
    id_request = models.IntegerField(default=0)


