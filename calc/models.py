from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return "姓名:%s,年龄:%s,性别:%s,联系方式:%s" % (self.name, self.age, self.sex, self.phone)
# Create your models here.
