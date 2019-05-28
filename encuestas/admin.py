from django.contrib import admin
from .models import Pacientes
from .models import Procedimientos
from .models import Encuestas



# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


class ProcedimientosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


class EncuestasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')







admin.site.register(Pacientes, PacientesAdmin)

admin.site.register(Procedimientos, ProcedimientosAdmin)

admin.site.register(Encuestas, EncuestasAdmin)


