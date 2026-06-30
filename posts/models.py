from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # Chi ha scritto il post (Collegamento all'utente)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # Contenuto del post
    testo = models.TextField(max_length=1000)

    # Data di creazione
    data_creazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.data_creazione.strftime('%d/%m/%Y')}"

class Meta:
    ordering = ['-data_creazione']