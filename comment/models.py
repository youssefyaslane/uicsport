from django.db import models

class Comment(models.Model):
    content = models.TextField()
    # Ajoutez d'autres champs si nécessaire (par exemple, nom de l'auteur, date, etc.)
