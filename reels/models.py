from django.db import models

# Create your models here.
class Reel(models.Model):
    by = models.CharField(max_length=25)
    message = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message