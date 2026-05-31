from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Collega questo profilo a un Utente in modo 1 a 1
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campi extra
    bio = models.TextField(max_length=500, blank=True)

    # Campo per i follow Molti a molti
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username