# parametres/serializers.py
from rest_framework import serializers
from scraping.models import *

class ParametreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametreType
        fields = '__all__'

class ParametreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametre
        fields = '__all__'

class ValeurParametreDansCombinaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValeurParametreDansCombinaison
        fields = '__all__'

class CombinaisonRechercheSerializer(serializers.ModelSerializer):
    parametres = ValeurParametreDansCombinaisonSerializer(many=True, read_only=True)

    class Meta:
        model = CombinaisonRecherche
        fields = ['id', 'nom', 'date_creation', 'parametres']
