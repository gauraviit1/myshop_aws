from django.db import models

# Create your models here.
class Testimonial_(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.comment

