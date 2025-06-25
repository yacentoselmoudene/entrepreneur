# parametres/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'types', ParametreTypeViewSet)
router.register(r'parametres', ParametreViewSet)
router.register(r'valeurs', ValeurParametreDansCombinaisonViewSet)
router.register(r'combinaisons', CombinaisonRechercheViewSet)

urlpatterns = router.urls
