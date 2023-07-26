from django.db import models
from django.urls import reverse

# Create your models here.
class Sonny(models.Model):
    name = models.CharField(max_length=75)
    series = models.CharField(max_length=75)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sonnyangel_id': self.id})