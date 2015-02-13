from django.db import models


# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
    text = models.TextField()


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=128)
    date = models.DateTimeField('date commented')
    ip_address = models.GenericIPAddressField()
    text = models.TextField()
