from django.contrib import admin
from matplotlib import pyplot
from .models import  Proyecto as ProyectoModel, Tipo_Proyecto as TipoModel, Encargado
from django.db.models import Sum

class EncargadoInline(admin.TabularInline):
    model=Encargado
    extra=0 

class ProyectoAdmin(admin.ModelAdmin):
    

    actions= ['graficas']
    date_hierarchy = 'fecha'
    list_filter=['fecha','tipo_proyecto','lugar']
    list_display = ['tipo_proyecto', 'lugar','donaciones','fecha', 'hora_inicio', 'proyectoinforme']
    filter_horizontal = ('participantes',)
    inlines = [EncargadoInline]



    def graficas(ModelAdmin, tipos, cantidad):
        tipos = TipoModel.objects.all()
        cantidad = ProyectoModel.objects.all()
        motivo = ['',]
        slices = []
        contador = 0
        suma = 0

        for elemento in tipos:
            motivo.append(elemento.nombre)
            for e in cantidad:
                var1 = elemento.nombre
                var2 = e.tipo_proyecto.nombre
                if var2 == var1:
                    suma += e.donaciones
            slices.append(suma)
            contador += 1
            suma = 0

        print(motivo)
        print(slices)
        _, _, texto = pyplot.pie(slices, labels=slices, autopct='%1.1f%%')

        for tex in texto:
            tex.set_color('white')

        pyplot.axis('equal')
        pyplot.title('Cantidad de Donaciones Realizadas')
        pyplot.legend(labels=motivo)
        pyplot.show()


admin.site.register(ProyectoModel, ProyectoAdmin)

class Tipo_ProyectoAdmin(admin.ModelAdmin):

    search_fields=['nombre']
    list_filter=['nombre']
    list_display=['nombre']

    def inactivar(self, request, queryset):

        for row in queryset.filter(activo=True):
            self.log_change(request, row, 'inactivar campo')
        rows_updated = 0

        for obj in queryset:
            if obj.activo:
                obj.activo = False
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 campo se marco"
        else:
            message_bit = "%s campos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como inactivas" % message_bit)
    inactivar.short_description = 'Inactivar campo'


    def activar(self, request, queryset):

        for row in queryset.filter(activo=False):
            self.log_change(request, row, 'activar campo')
        rows_updated = 0

        for obj in queryset:
            if not obj.activo:
                obj.activo = True
                obj.save()

                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 campo se marco"
        else:
            message_bit = "%s campos se marcaron" % rows_updated
        self.message_user(
            request, "%s satisfactoriamente como activos" % message_bit)
    activar.short_description = 'Activar campo'

admin.site.register(TipoModel, Tipo_ProyectoAdmin)