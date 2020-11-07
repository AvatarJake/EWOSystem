from datetime import datetime

from django.utils.html import format_html
from django.contrib import admin
from matplotlib import pyplot

from .models import *
from tkinter import *



class CategoriaAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']
    search_fields=['nombre']
    list_filter=['nombre']
    list_display=['nombre']
    
    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar Tipo')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 Tipo se marco"
        else:
            message_bit = "%s Tipos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar Tipo'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar Tipo')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 Tipo se marco"
        else:
            message_bit = "%s Tipos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar Tipo'

admin.site.register(Categoria, CategoriaAdmin)

class MovimientoInline(admin.TabularInline):
    model=Movimiento
    extra=0

class PresupuestoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    inlines=[MovimientoInline]
    search_fields=['fecha']
    list_filter=['fecha']
    list_display = ['descripcion','fecha','saldo', 'presupuestoinforme']








admin.site.register(Presupuesto, PresupuestoAdmin)