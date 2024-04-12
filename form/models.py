from django.db import models

# Create your models here.
class Inscription(models.Model):
    FULL_NAME_CHOICES = (
        ('foot', 'Football'),
        ('basket', 'Basketball'),
        ('tennis', 'Tennis'),
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    discipline = models.CharField(max_length=10, choices=FULL_NAME_CHOICES)