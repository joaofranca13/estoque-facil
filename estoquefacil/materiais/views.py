from django.shortcuts import render
from .models import Materiais


def index(request):
    entradas_recentes = Materiais.objects.order_by('-datacompra')[0:10]
    context = {'entradas_recentes': entradas_recentes}
    return render(request, 'materiais/index.html', context)
