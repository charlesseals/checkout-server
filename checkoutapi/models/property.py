from django.db import models

class Property(models.Model):
    user = models.ForeignKey("CheckoutUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=100)
    size = models.PositiveIntegerField(default=0)
    image_url = models.CharField(max_length=500)
