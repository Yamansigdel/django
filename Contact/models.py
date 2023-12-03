from django.db import models


class Contactenquire(models.Model):
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=100)