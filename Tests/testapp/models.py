from django.db import models

# Create your models here.

class Happy(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now_add=True)
#Add a daunder
    def __str__(self):
        return self.first_name
