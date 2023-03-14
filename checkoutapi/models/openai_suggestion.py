from django.db import models

class OpenaiSuggestion(models.Model):
    content = models.CharField(max_length=500)