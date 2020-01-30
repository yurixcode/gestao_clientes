from django.contrib import admin

# Models
from .models import Venda
from .models import ItemDoPedido

# Actions
from .actions import nfe_emitida, nfe_nao_emitida

class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 2


class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc',)
    # list_display = ('numero', 'pessoa', 'get_total', 'nfe_emitida')
    list_display = ('numero', 'pessoa', 'nfe_emitida')
    # raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)

    readonly_fields = ('valor',)
    search_fields = ('numero', 'pessoa__first_name', 'pessoa__last_name', 'pessoa__doc__num_doc')

    actions = [nfe_emitida, nfe_nao_emitida]
    # filter_horizontal = ['produtos']
    
    inlines = [ItemPedidoInline]


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)
