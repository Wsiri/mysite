from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return
# Create your models here.
