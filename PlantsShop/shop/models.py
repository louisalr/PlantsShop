import os
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


"""
#to rename the picture automatically
def random_name(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return '{}.{}'.format(instance.pk, ext)
    else:
        pass
        # do something if pk is not there yet

    return os.path.join('/articles/', filename)
"""


class Article(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    price = models.FloatField()
    question = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    stock = models.IntegerField()
    picture = models.ImageField(blank=True, upload_to='articles')

    def __str__(self):
        return self.name

#class Order(models.Model):
    #user = models.ForeignKey(AUTH_USER_MODEL)
