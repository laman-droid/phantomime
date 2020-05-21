from django.db import models

# Create your models here.
class Nowshow(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()

class Upcomingshow(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
