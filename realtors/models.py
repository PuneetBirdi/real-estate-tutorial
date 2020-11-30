from django.db import models
from datetime import datetime

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=128)
    phone: models.CharField(max_length=24)
    is_mvp: models.BooleanField(default=False)
    hire_date: models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
