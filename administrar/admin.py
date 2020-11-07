from django.contrib import admin
from .models import *

# Register your models here.
class CargoAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']
    search_fields=['nombre']
    list_filter=['nombre']
    list_display=['nombre']
    
    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar cargo')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 cargo se marco"
        else:
            message_bit = "%s cargos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar cargo'

    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar cargo')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 cargo se marco"
        else:
            message_bit = "%s cargos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar cargo'

admin.site.register(Cargo, CargoAdmin)


class IglesiaAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']

    search_fields = ['nombre', 'lugar']
    list_filter = ['lugar']
    list_display = ['nombre', 'lugar', 'activo']

     
    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar empleado')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 iglesia se marco"
        else:
            message_bit = "%s iglesias se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar iglesia'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar iglesia')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 iglesia se marco"
        else:
            message_bit = "%s iglesias se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar iglesia'

admin.site.register(Iglesia, IglesiaAdmin)


class LugarAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']

    search_fields = ['nombre']
    list_filter = ['origen']
    list_display = ['nombre', 'origen']

     ###
    # acciones
    ###

    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar empleado')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 lugar se marco"
        else:
            message_bit = "%s lugares se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar lugar'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar lugar')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 lugar se marco"
        else:
            message_bit = "%s lugares se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar lugar'

admin.site.register(Lugar, LugarAdmin)

class MiembroAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']
    search_fields = ['nombres', 'apellidos']
    list_filter = ['genero', 'cargo']
    list_display = ['nombres', 'apellidos','cargo','genero','telefono','lugar','activo']

   #seccion de acciones 

    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar miembro')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 miembro se marco"
        else:
            message_bit = "%s miembros se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar miembro'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar miembro')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 miembro se marco"
        else:
            message_bit = "%s miembros se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar miembro'

admin.site.register(Miembro, MiembroAdmin)

class PersonaAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']
    list_filter = ['genero', 'tipo', 'lugar']
    list_display = ['nombres','apellidos','telefono','tipo','lugar','activo']
    search_fields = ['nombres', 'apellidos']

   #seccion de acciones 

    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar persona')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 persona se marco"
        else:
            message_bit = "%s personas se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar persona'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar persona')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 persona se marco"
        else:
            message_bit = "%s personas se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar persona'

admin.site.register(Persona, PersonaAdmin)



class TipoPersonaAdmin(admin.ModelAdmin):
    actions = ['inactivar', 'activar']
    search_fields=['tipo']
    list_filter=['tipo',]
    list_display=['tipo']

    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar tipo de persona')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 tipos de personas se marco"
        else:
            message_bit = "%s tipos de personas se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar tipo de persona'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar lugar')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 tipo de persona se marco"
        else:
            message_bit = "%s tipos de personas se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar tipo persona'
admin.site.register(TipoPersona, TipoPersonaAdmin)