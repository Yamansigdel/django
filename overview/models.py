from django.db import models

# Create your models here.
class Overview(models.Model):
    overview_title = models.CharField(max_length=50)
    overview_des = models.TextField()