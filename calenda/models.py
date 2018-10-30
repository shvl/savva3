from django.db import models
import datetime
# Create your models here.


# First, define the Manager subclass.
class FutureManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start__date__gt=datetime.date.today())

class Event(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    start = models.DateTimeField()
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=300, blank=True)

    place = models.CharField(max_length=300, blank=True)

    comment = models.TextField(blank=True)

    #managers
    objects = models.Manager()
    future = FutureManager()

    def __str__(self):
        return self.city
