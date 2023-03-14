from django.db import models

class Cleaner(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)