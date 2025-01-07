from django.db import models

class Movies(models.Model):
    title =  models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    release_year =  models.IntegerField(max_length=4)
    # image =  models.ImageField(upload_to='photos/%y/%m/%d')
    # active = models.BooleanField(default=True)

