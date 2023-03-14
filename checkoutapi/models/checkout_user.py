from django.db import models
from django.contrib.auth.models import User

class CheckoutUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    profile_image_url = models.CharField(max_length=200, null=True, default="No URL Provided")

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'