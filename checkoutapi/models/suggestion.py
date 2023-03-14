from django.db import models

class Suggestion(models.Model):
    user = models.ForeignKey("CheckoutUser", on_delete=models.CASCADE)
    openai_suggestion = models.ForeignKey("OpenaiSuggestion", on_delete=models.CASCADE)