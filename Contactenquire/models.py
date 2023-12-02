from django.db import models

class Contact(models.Model):
    contact_title=models.CharField(max_length=100)
    contact_desc=models.TextField()
