from django.http import HttpResponseForbidden

def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseForbidden("<h1>NO AUTORIZADO!!! SÉ QUIEN ERES!!</h1>")

nfe_emitida.short_description = 'NF-e emitido'


def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

nfe_nao_emitida.short_description = 'NF-e nao emitido'