from django.db import models
from uuid import *


# Create your models here.


class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    job = models.CharField(max_length=225)

    def __str__(self):
        return self.name
