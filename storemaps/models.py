from django.db import models
# Create your models here.


class Maps(models.Model):
		url = models.URLField(max_length=500)
		controller_jail = models.CharField(max_length=100)
		name = models.CharField(max_length=100)