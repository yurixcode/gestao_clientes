from django.contrib import admin
from .models import Person, Documento


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


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)