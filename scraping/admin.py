from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ParametreType, Parametre, CombinaisonRecherche, ValeurParametreDansCombinaison

admin.site.register(ParametreType)
admin.site.register(Parametre)
admin.site.register(CombinaisonRecherche)
admin.site.register(ValeurParametreDansCombinaison)