from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(null=False, max_length=4096)
    size = models.IntegerField(null=False)
