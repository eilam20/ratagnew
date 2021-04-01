from django.contrib.gis.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
# Create your models here.

class Site(models.Model):
    title = models.CharField(max_length=200)
    Polygon = models.PolygonField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('gisapp:Site_detail', kwargs={'pk': self.pk})


class Hazard(models.Model):

    point = models.PointField()
    title = models.CharField(max_length=50)
    created_time = models.DateTimeField(default= timezone.now)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):

        return reverse('gisapp:Hazard_detail', kwargs={'pk': self.pk})

