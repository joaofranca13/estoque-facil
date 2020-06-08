from django.shortcuts import render
from .models import Materiais
# from django.http import HttpResponse
from .forms import EntradaMateriais
from django.shortcuts import redirect, reverse
from django.db.models import Sum


def index(request):
    return render(request, 'materiais/index.html')


def meuestoque(request):
    estoque = Materiais.objects.values('material').annotate(
        Sum('custo')).annotate(Sum('quantidade'))
    saldo = Materiais.objects.aggregate(total=Sum('custo'))
    return render(request, 'materiais/meuestoque.html',
                  {'estoque': estoque,
                   'saldo': saldo,
                   }
                  )


def detailview(request, nome):
    detail = Materiais.objects.filter(material=nome)
    return render(request, 'materiais/detalhe.html', {'detail': detail})


def entrada(request):
    if request.method == 'POST':
        form = EntradaMateriais(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('materiais:entrada'))
    else:
        form = EntradaMateriais()
    return render(request, 'materiais/entrada.html', {'form': form})
