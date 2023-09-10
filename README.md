# ✨😇Sonny Angel Collector😇✨
## Description
Welcome to the Sonny Angel Collector App, the ultimate hub for all passionate Sonny Angel enthusiasts! Whether you're a dedicated collector, a creative designer, or a perfectionist quality inspector, this app is your digital haven for managing and celebrating your beloved Sonny Angel figurines.
## Getting Started
Launch the deployed site linked down below :
[Sonny Angel Collector](https://sonny-angel-collector-c61cb0dd8988.herokuapp.com/)

## Preview

## Technologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) 
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

## Code Preview
```python
from django.db import models
from django.urls import reverse

CONDITIONS = (
    ('N', 'Like New'),
    ('S', 'Slightly Damaged'),
    ('D', 'Damaged')
)

# Create your models here.
class Outfit(models.Model):
    type = models.CharField(max_length= 50)
    color = models.CharField(max_length= 25)

    def __str__(self):
        return self.type
    
    def get_absolute_url(self):
        return reverse('outfits_detail', kwargs={'pk': self.id})


class Sonny(models.Model):
    name = models.CharField(max_length=75)
    series = models.CharField(max_length=75)
    description = models.TextField(max_length=200)
    outfits = models.ManyToManyField(Outfit)

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

```
## Icebox Features
- Create User Profiles
- Create feature of connecting to other collectors
- Add a chat or message feature between collectors
