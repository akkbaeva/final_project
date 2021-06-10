from django.db import models


# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    achievement = models.TextField()

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    date_published = models.DateField(auto_now_add=True)
    singer = models.ManyToManyField(Singer, verbose_name='singer_album', null=True, blank=True)
