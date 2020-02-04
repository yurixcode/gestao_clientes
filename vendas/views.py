# Django
from django.shortcuts import render
from django.db.models import Sum, F, FloatField, Min, Max, Avg, Count

from django.http import HttpResponse

# Views
from django.views import View

# Models
from .models import Venda

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('No tienes los permisos necesarios...')
        
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['mini'] = Venda.objects.minimo()
        data['maxi'] = Venda.objects.maximo()
        data['n_pedidos'] = Venda.objects.numero_pedidos()
        data['n_pedidos_fiscal'] = Venda.objects.pedidos_enviados()

        return render(request, 'vendas/dashboard.html', data)