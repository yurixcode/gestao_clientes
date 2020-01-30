from django.contrib import admin
from .models import Person, Documento, Venda, ItemsDoPedido

# Actions
from .actions import nfe_emitida, nfe_nao_emitida

class PersonAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Información básica', {
        'fields' : ('doc', ('first_name', 'last_name'), ('age', 'salary'))
        }),

        ('Información avanzada', {
            'classes' : ('collapse',),
            'fields' : ('bio', 'photo')
        }),
    )

    """En list_display señalamos los campos que queremos mostrar previo a acceder los datos"""
    list_filter = ('age', 'salary')
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'has_photo')

    search_fields = ('id', 'first_name')

    def has_photo(self, obj):
        if obj.photo:
            return 'Si'
        else:
            return ''

    has_photo.short_description = 'Tiene FOTO'




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



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemsDoPedido)