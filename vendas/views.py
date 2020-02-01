# Django
from django.shortcuts import render
from django.db.models import Sum, F, FloatField, Min, Max, Avg, Count

# Views
from django.views import View

# Models
from .models import Venda

class DashboardView(View):
    def get(self, request):
        data = {}

        data['media'] = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        data['media_desc'] = Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg']
        data['mini'] = Venda.objects.all().aggregate(Min('valor'))['valor__min']
        data['maxi'] = Venda.objects.all().aggregate(Max('valor'))['valor__max']
        data['n_pedidos'] = Venda.objects.all().aggregate(Count('id'))['id__count']
        data['n_pedidos_fiscal'] = Venda.objects.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']

        return render(request, 'vendas/dashboard.html', data)