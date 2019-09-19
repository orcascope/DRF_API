from django.shortcuts import render
from .models import Projects, FA
from django.http import JsonResponse

def projects_list(request):
    projs = Projects.objects.all()[:20]
    data = {"results" : list(projs.values())}
    return JsonResponse(data)

def fa_list(request):
    fa = FA.objects.all()[:20]
    data =  {"results" : list(fa.values())}
    return JsonResponse(data)

