from django.db import models
from django.urls import reverse

CONDITIONS = (
    ('N', 'Like New'),
    ('S', 'Slightly Damaged'),
    ('D', 'Damaged')
)

# Create your models here.
class Sonny(models.Model):
    name = models.CharField(max_length=75)
    series = models.CharField(max_length=75)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sonnyangel_id': self.id})
    

class Inspect(models.Model):
    date = models.DateField('Inspect Date')
    condition = models.CharField(
        max_length=1,
        choices=CONDITIONS,
        default=CONDITIONS[0][0]
    )
    sonnyangel = models.ForeignKey(Sonny, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_condition_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
