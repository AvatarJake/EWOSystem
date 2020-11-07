from django.contrib import admin
from .models import *
#from actividades.models import Responsable
from django.template.loader import get_template
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin

class ResponsableInline(admin.TabularInline):
    model=Responsable
    extra=0 
class ActividadResource(resources.ModelResource):
    class Meta:
        model = Actividad

class ActividadAdmin(ImportExportModelAdmin,ExportMixin,admin.ModelAdmin):

    date_hierarchy = 'fecha'
    list_filter=['fecha','tipo_actividad']
    list_display = ['tipo_actividad','lugar','fecha','hora_inicio','actividadinforme']
    resource_class = ActividadResource
    inlines = [ResponsableInline]
    filter_horizontal=('participantes',)

admin.site.register(Actividad, ActividadAdmin) 

class Tipo_ActividadAdmin(admin.ModelAdmin):

    search_fields=['nombre']
    list_filter=['nombre']
    list_display=['nombre']



admin.site.register(Tipo_Actividad, Tipo_ActividadAdmin)