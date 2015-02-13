from django.db import models

import datetime
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
    text = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=128)
    date = models.DateTimeField('date commented')
    ip_address = models.GenericIPAddressField()
    text = models.TextField()

    def __str__(self):
        return self.text
