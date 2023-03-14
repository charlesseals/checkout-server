from django.db import models

class CleaningAppointment(models.Model):
            cleaner = models.ForeignKey("Cleaner", on_delete=models.CASCADE)
            property = models.ForeignKey("Property", on_delete=models.CASCADE)
            date_time = models.DateTimeField(auto_now_add=False, default="No Date and Time Selected")
            progress = models.BooleanField(null=False)
