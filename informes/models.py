import os

from django.db import models

from actividades.models import Tipo_Actividad, Actividad
from presupuesto.models import Categoria, Movimiento
from proyectos_sociales.models import Tipo_Proyecto, Proyecto
from .models import *
# Create your models here.
from django.utils.safestring import mark_safe
from matplotlib import pyplot
from os import remove

class Informes(models.Model):


    def eventosInforme(self):
        return mark_safe('<a target="_blank" href="/informes/eventos" class="Imprimir">Informe General de Actividades</a>')

    def eventosPendientesInforme(self):
        return mark_safe(
            '<a target="_blank" href="/informes/eventos_pendientes" class="Imprimir">Informe de Actividades Pendientes</a>')

    def eventosRealizadosInforme(self):
        return mark_safe(
            '<a target="_blank" href="/informes/eventos_realizados" class="Imprimir">Informe de Actividades Realizadas</a>')

    class Meta:
        db_table = 'informe_general'
        verbose_name= 'Informes_generales'
        verbose_name_plural= 'Informes de Eventos'

class InformePastores(models.Model):

    def pastoresInforme(self):
        return mark_safe('<a target="_blank" href="/informes/pastores" class="Imprimir">Informe de Pastores</a>')

    class Meta:
        db_table = 'informe_pastor'
        verbose_name= 'Informe_pastores'
        verbose_name_plural= 'Informe Pastores'


class ProyectoPorRango(models.Model):
    nombre='Seleccione un rango de fechas'
    fecha_inicio = models.DateField('Fecha De Inicio')
    fecha_limite = models.DateField('Fecha De Limite')

    def proyectoInforme(self):
        return mark_safe('<a target="_blank" href="/informes/proyectos_rango/'+str(self.id)+'" class="Imprimir">Proyectos por rango</a>')

    def save(self, *args, **kwargs):

        # now = datetime.now()
        tipos = Tipo_Proyecto.objects.all()
        proyecto = Proyecto.objects.all()
        motivo = []
        slices = []
        colores = ('blue', 'green', 'red', '#30f8ff', '#59ff30', '#e8f00e', '#ff5405')
        contador = 0
        suma = 0

        for elemento in tipos:
            motivo.append(elemento.nombre)

            for e in proyecto:
                var1 = elemento.nombre
                var2 = e.tipo_proyecto.nombre
                if (var2 == var1 and e.fecha >= self.fecha_inicio and e.fecha <= self.fecha_limite):
                    suma += e.donaciones
                print(suma)
            slices.append(suma)
            suma = 0
            print(slices)
            print(motivo)

        pyplot.rcParams['toolbar']
        _, _, texto = pyplot.pie(slices, labels=slices, colors=colores, autopct='%1.1f%%')

        for tex in texto:
            tex.set_color('white')

        pyplot.legend(labels=motivo)
        pyplot.axis('equal')
        pyplot.title('Proyectos Realizados')
        pyplot.savefig('media/graficas/rangoproyecto.png')
        pyplot.clf()
        super(ProyectoPorRango, self).save(*args, **kwargs)

    class Meta():
        db_table = 'proyecto_por_rango'
        verbose_name = 'Proyecto Por Rango de Fecha'
        verbose_name_plural = 'Proyectos Por Rango de Fecha'


class InformeTipoProyecto(models.Model):
    nombre = 'Seleccione un rango de fechas y un tipo de proyecto'
    fecha_inicio = models.DateField('Fecha De Inicio')
    fecha_limite = models.DateField('Fecha De Limite')
    tipo = models.ForeignKey(Tipo_Proyecto, on_delete=models.CASCADE)

    def proyectoInforme(self):
        return mark_safe('<a target="_blank" href="/informes/tipo_proyecto_rango/'+str(self.id)+'" class="Imprimir">Proyectos por tipo</a>')

    def save(self, *args, **kwargs):

        proyecto = Proyecto.objects.all()
        motivo = []
        slices = []
        colores = ('blue', 'green', 'red', '#30f8ff', '#59ff30', '#e8f00e', '#ff5405')
        contador = 0
        suma = 0
        meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        inicio = self.fecha_inicio.month
        fin = self.fecha_limite.month
        print(inicio)
        print(fin)

        for e in meses:
            if (e >= inicio and e <= fin):
                if e == 1:
                    motivo.append('Enero')
                if e == 2:
                    motivo.append('Febrero')
                if e == 3:
                    motivo.append('Marzo')
                if e == 4:
                    motivo.append('Abril')
                if e == 5:
                    motivo.append('Mayo')
                if e == 6:
                    motivo.append('Junio')
                if e == 7:
                    motivo.append('Julio')
                if e == 8:
                    motivo.append('Agosto')
                if e == 9:
                    motivo.append('Septiembre')
                if e == 10:
                    motivo.append('Octubre')
                if e == 11:
                    motivo.append('Noviembre')
                if e == 12:
                    motivo.append('Dicimbre')

                for elemento in proyecto:
                    if (self.tipo.nombre == elemento.tipo_proyecto.nombre and elemento.fecha.month == e):
                        contador += elemento.donaciones
                slices.append(contador)
                contador = 0

        pyplot.rcParams['toolbar']
        _, _, texto = pyplot.pie(slices, labels=slices, colors=colores, autopct='%1.1f%%')
        for tex in texto:
            tex.set_color('white')

        pyplot.legend(labels=motivo)
        pyplot.axis('equal')
        pyplot.title(self.tipo.nombre)
        pyplot.savefig('media/graficas/tipo_proyecto_rango.png')
        pyplot.clf()

        super(InformeTipoProyecto, self).save()

    class Meta():
        db_table = 'informe_por_tipo'
        verbose_name = 'Informe Por Tipo'
        verbose_name_plural = 'Informes Tipo'

class ActividadPorRango(models.Model):
    nombre='Seleccione un rango de fechas'
    fecha_inicio = models.DateField('Fecha De Inicio')
    fecha_limite = models.DateField('Fecha De Limite')

    def actividadInforme(self):
        return mark_safe('<a target="_blank" href="/informes/actividades_rango/'+str(self.id)+'" class="Imprimir">Actividades por rango</a>')

    def save(self, *args, **kwargs):

        # now = datetime.now()
        tipos = Tipo_Actividad.objects.all()
        proyecto = Actividad.objects.all()
        motivo = []
        slices = []
        colores = ('blue', 'green', 'red', '#30f8ff', '#59ff30', '#e8f00e', '#ff5405')
        contador = 0
        suma = 0

        for elemento in tipos:
            motivo.append(elemento.nombre)

            for e in proyecto:
                var1 = elemento.nombre
                var2 = e.tipo_actividad.nombre
                if (var2 == var1 and e.fecha >= self.fecha_inicio and e.fecha <= self.fecha_limite):
                    contador += 1
                print(contador)
            slices.append(contador)
            contador = 0
            print(slices)
            print(motivo)

        pyplot.rcParams['toolbar']
        _, _, texto = pyplot.pie(slices, labels=slices, colors=colores, autopct='%1.1f%%')

        for tex in texto:
            tex.set_color('white')

        pyplot.legend(labels=motivo)
        pyplot.axis('equal')
        pyplot.title('Grafica de Actividades Realizadas')
        pyplot.savefig('media/graficas/rangoactividad.png')
        pyplot.clf()
        super(ActividadPorRango, self).save(*args, **kwargs)

    class Meta():
        db_table = 'actividad_por_rango'
        verbose_name = 'Actividad Por Rango de Fecha'
        verbose_name_plural = 'Actividades Por Rango de Fecha'

class PresupuestoPorRango(models.Model):
    nombre='Seleccione un rango de fechas'
    fecha_inicio = models.DateField('Fecha De Inicio')
    fecha_limite = models.DateField('Fecha De Limite')
    gasto=models.FloatField(default=0.00)

    def presupuestoInforme(self):
        return mark_safe('<a target="_blank" href="/informes/presupuesto_rango/'+str(self.id)+'" class="Imprimir">Presupuesto por rango</a>')

    def save(self, *args, **kwargs):

        # now = datetime.now()
        tipos = Categoria.objects.all()
        mov = Movimiento.objects.all()
        motivo = [' ']
        slices = []
        colores = ('white', 'green', 'red', '#30f8ff', '#59ff30', '#e8f00e', '#ff5405')
        contador = 0
        suma = 0
        total=0
        for elemento in tipos:
            if elemento.tipo != "Ingreso":
                motivo.append(elemento.nombre)
            for e in mov:
                var1 = elemento.nombre
                var2 = e.motivo.nombre
                if (var2 == var1 and e.fecha >= self.fecha_inicio and e.fecha <= self.fecha_limite):
                    if e.tipo != "Ingreso":
                        suma += (e.cantidad)
            total+=(suma)
            slices.append(suma)
            suma = 0
            self.gasto=total
            print(slices)
            print(motivo)
            print(total)
        pyplot.rcParams['toolbar']
        _, _, texto = pyplot.pie(slices, labels=slices, colors=colores, autopct='%1.1f%%')

        for tex in texto:
            tex.set_color('white')

        pyplot.legend(labels=motivo)
        pyplot.axis('equal')
        pyplot.title('Grafica de Presupuesto')
        pyplot.savefig('media/graficas/rangopresupuesto.png')
        pyplot.clf()
        super(PresupuestoPorRango, self).save(*args, **kwargs)

    class Meta():
        db_table = 'presupuesto_por_rango'
        verbose_name = 'Presupuesto Por Rango de Fecha'
        verbose_name_plural = 'Presupuesto Por Rango de Fecha'