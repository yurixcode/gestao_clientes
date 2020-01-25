from django.contrib import admin
from .models import Person, Documento, Venda, Produto

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
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'photo')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)