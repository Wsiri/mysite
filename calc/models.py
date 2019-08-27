from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return "姓名:%s,年龄:%s,性别:%s,联系方式:%s" % (self.name, self.age, self.sex, self.phone)


class Blog(models.Model):
    name = models.CharField(max_length=300)
    tagLine = models.TextField()

    def __str__(self):
        return self.name


class Author (models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=300)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingBacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


# Create your models here.
