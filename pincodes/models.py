from django.db import models

# Create your models here.
class Pincode(models.Model):
    pincode = models.PositiveIntegerField()
    officeName = models.CharField(max_length=60)
    deliveryStatus = models.CharField(max_length=15)
    taluk = models.CharField(max_length=50)
    districtName = models.CharField(max_length=30)
    stateName = models.CharField(max_length=30)

    def __str__(self):
        return str(self.pincode)
