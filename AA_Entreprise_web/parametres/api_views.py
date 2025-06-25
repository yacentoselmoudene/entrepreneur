# parametres/api_views.py
from rest_framework import viewsets
from AA_Entreprise_web.models import *
from .serializers import *

class ParametreTypeViewSet(viewsets.ModelViewSet):
    queryset = ParametreType.objects.all()
    serializer_class = ParametreTypeSerializer

class ParametreViewSet(viewsets.ModelViewSet):
    queryset = Parametre.objects.all()
    serializer_class = ParametreSerializer

class ValeurParametreDansCombinaisonViewSet(viewsets.ModelViewSet):
    queryset = ValeurParametreDansCombinaison.objects.all()
    serializer_class = ValeurParametreDansCombinaisonSerializer

class CombinaisonRechercheViewSet(viewsets.ModelViewSet):
    queryset = CombinaisonRecherche.objects.all()
    serializer_class = CombinaisonRechercheSerializer
