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

from django.db import models

class ParametreType(models.Model):
    """
    Type de paramètre (ex : Bon de Commande, Marché, etc.)
    """
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Parametre(models.Model):
    """
    Paramètre utilisable pour une recherche (ex : 'p1', 'num_marche', 'date_livraison', etc.)
    """
    nom = models.CharField(max_length=100)  # p1, p2 ou un nom réel
    description = models.TextField(blank=True, null=True)
    html_input_id = models.CharField(max_length=100, help_text="ID ou name HTML du champ à cibler")
    type_parametre = models.ForeignKey(ParametreType, on_delete=models.CASCADE, related_name='parametres')

    def __str__(self):
        return f"{self.nom} ({self.type_parametre.nom})"


class CombinaisonRecherche(models.Model):
    """
    Une recherche personnalisée avec une ou plusieurs valeurs de paramètres
    """
    nom = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class ValeurParametreDansCombinaison(models.Model):
    """
    Valeur d'un paramètre dans une combinaison
    """
    combinaison = models.ForeignKey(CombinaisonRecherche, on_delete=models.CASCADE, related_name="parametres")
    parametre = models.ForeignKey(Parametre, on_delete=models.CASCADE)
    valeur = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.parametre.nom} = {self.valeur} (dans {self.combinaison.nom})"

class Caution(models.Model):
    reference = models.CharField(max_length=100, unique=True)  # Référence de la caution
    procedure_type = models.CharField(max_length=255)  # Type de procédure (ex: AOS)
    categorie = models.CharField(max_length=255)  # Catégorie (ex: Fournitures)
    objet = models.TextField()  # Objet de l'appel d'offre
    organisme = models.CharField(max_length=255)  # Organisme (ex: REGION de SOUS-MASSA-DRAA)
    date_limite = models.DateTimeField()  # Date limite de remise des plis
    banque = models.CharField(max_length=255)  # Nom de la banque
    compte_bancaire = models.CharField(max_length=255, blank=True, null=True)  # Numéro de compte bancaire
    montant = models.DecimalField(max_digits=12, decimal_places=2)  # Montant de la caution
    intitule = models.CharField(max_length=255)  # Intitulé de la caution
    statut = models.CharField(max_length=255)  # Statut (ex: Validée par la banque)
    lien_telechargement = models.URLField(blank=True, null=True)  # Lien pour télécharger la caution
    lien_restitution = models.URLField(blank=True, null=True)  # Lien pour la demande de restitution
    date_scraping = models.DateTimeField(auto_now_add=True)  # Date d'extraction

    def __str__(self):
        return f"{self.reference} - {self.intitule}"
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
    sended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reference} - {self.objet[:50]}"
