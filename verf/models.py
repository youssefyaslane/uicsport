from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Terrain(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Reservation(models.Model):
    terrain = models.ForeignKey(Terrain, on_delete=models.CASCADE)
    date_heure_debut = models.DateTimeField()
    date_heure_fin = models.DateTimeField()


    
