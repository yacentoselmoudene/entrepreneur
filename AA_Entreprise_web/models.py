import os
from argparse import Action
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db.models import UniqueConstraint
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.timezone import now

class SourceSite(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()
    actif = models.BooleanField(default=True)

class Marche(models.Model):
    reference = models.CharField(max_length=255)
    objet = models.TextField()
    maitre_ouvrage = models.CharField(max_length=255)
    lieu_execution = models.CharField(max_length=255, blank=True, null=True)
    date_limite = models.DateField()
    source_site = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.reference} - {self.objet[:50]}"
