from django.db import models

# Create your models here.
class Pincode(models.Model):
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return str(self.pincode)
