from django.contrib import admin

# Register your models here.
from informes.models import *


class InformesAdmin(admin.ModelAdmin):

    list_display=['eventosInforme', 'eventosPendientesInforme', 'eventosRealizadosInforme']


admin.site.register(Informes, InformesAdmin)

class InformePastoresAdmin(admin.ModelAdmin):
    list_display=['pastoresInforme']


admin.site.register(InformePastores, InformePastoresAdmin)

class ProyectoPorRangoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_inicio', 'fecha_limite', 'proyectoInforme']

admin.site.register(ProyectoPorRango, ProyectoPorRangoAdmin)

class  InformeTipoPoryectoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_inicio', 'fecha_limite', 'proyectoInforme']

admin.site.register(InformeTipoProyecto, InformeTipoPoryectoAdmin)

class ActividadPorRangoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_inicio', 'fecha_limite', 'actividadInforme']

admin.site.register(ActividadPorRango, ActividadPorRangoAdmin)

class PresupuestoPorRangoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_inicio', 'fecha_limite', 'presupuestoInforme']

admin.site.register(PresupuestoPorRango, PresupuestoPorRangoAdmin)