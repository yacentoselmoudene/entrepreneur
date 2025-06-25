from django.shortcuts import render
from django.http import JsonResponse
from .models import ParametreType, Parametre, CombinaisonRecherche, ValeurParametreDansCombinaison
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
import json

@login_required
@permission_required('parametres.view_parametres', raise_exception=True)
def parametres_dashboard(request):
    types = ParametreType.objects.all()
    parametres = Parametre.objects.select_related("type_parametre").all()
    return render(request, 'parametres/dashboard.html', {'types': types, 'parametres': parametres})

@csrf_exempt
@login_required
@permission_required('parametres.add_parametreetype', raise_exception=True)
def create_parametre_type(request):
    data = json.loads(request.body)
    ParametreType.objects.create(nom=data['nom'])
    return JsonResponse({"status": "success"})

@csrf_exempt
@login_required
@permission_required('parametres.add_parametre', raise_exception=True)
def create_parametre(request):
    data = json.loads(request.body)
    type_obj = ParametreType.objects.get(id=data['type_id'])
    Parametre.objects.create(
        nom=data['nom'],
        description=data['description'],
        html_input_id=data['html_input_id'],
        type_parametre=type_obj
    )
    return JsonResponse({"status": "success"})

@csrf_exempt
@login_required
@permission_required('parametres.add_combinaisonrecherche', raise_exception=True)
def create_combinaison(request):
    data = json.loads(request.body)
    combinaison = CombinaisonRecherche.objects.create(nom=data['nom'])
    for p in data['parametres']:
        param = Parametre.objects.get(id=p['parametre_id'])
        ValeurParametreDansCombinaison.objects.create(
            combinaison=combinaison,
            parametre=param,
            valeur=p['valeur']
        )
    return JsonResponse({"status": "success"})

@login_required
def load_combinaisons(request):
    combs = CombinaisonRecherche.objects.prefetch_related('parametres__parametre').all()
    results = []
    for c in combs:
        params = [
            {
                "nom": vp.parametre.nom,
                "valeur": vp.valeur,
                "html_id": vp.parametre.html_input_id
            }
            for vp in c.parametres.all()
        ]
        results.append({"nom": c.nom, "params": params})
    return JsonResponse(results, safe=False)