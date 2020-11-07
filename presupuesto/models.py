from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.db import models
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib.request
from urllib.request import urlopen

from .models import *
from django.utils.safestring import mark_safe

TIPO=(
('Ingreso', 'Ingreso'),
('Egreso', 'Egreso'),
	)
class Categoria(models.Model):
	nombre = models.CharField('Categoria', max_length=30)
	tipo = models.CharField('Tipo de movimiento', max_length=8, choices=TIPO, default='Ingreso')
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s %s' % (self.nombre,' ')

	def clean(self): # limpiar los campos antes de insertar o actualizar
		super(Categoria, self).clean()

	def save(self, **kwargs): # Guardar los campos despeus de insertar o actualizar

		if self.activo:
			self.nombre.upper()
		else:
			self.nombre = self.nombre.lower()
			
		super(Categoria, self).save()

	class Meta():
		db_table = 'categoria'
		verbose_name= 'Categoria'
		verbose_name_plural= 'Categorias'

class Presupuesto(models.Model):
	descripcion = models.CharField('Descripcion', max_length=50, blank=True, null=True)
	fecha = models.DateField('Fecha', null=True, blank=True)
	saldo = models.FloatField('Saldo', default=0.00)

	def __str__(self):
		return '%s %s' % (self.descripcion, self.saldo)


	def save(self, *args, **kwargs):
		ingresos=0
		egresos=0
		movimientos = self.movimiento_set.all()

		for e in movimientos:
			if e.tipo == "Ingreso":
				ingresos = (ingresos + e.cantidad)

			else:
				egresos = (egresos+e.cantidad)


		self.saldo=ingresos-egresos

		super(Presupuesto, self).clean()
		super(Presupuesto,self).save()
		# creacion de la grafica
		tipos = Categoria.objects.all()
		mov = Movimiento.objects.all()
		motivo = [' ']
		slices = []
		colores = ('white', 'green', 'red', '#30f8ff', '#59ff30', '#e8f00e', '#ff5405')
		contador = 0
		suma = 0

		for elemento in tipos:
			if elemento.tipo != "Ingreso":
				motivo.append(elemento.nombre)
			for e in mov:
				var1 = elemento.nombre
				var2 = e.motivo.nombre
				if var2 == var1:
					if e.tipo != "Ingreso":
						suma += (e.cantidad)
			slices.append(suma)
			suma = 0

		pyplot.rcParams['toolbar']
		_, _, texto = pyplot.pie(slices, labels=slices, colors=colores, autopct='%1.1f%%')

		for tex in texto:
			tex.set_color('white')

		pyplot.legend(labels=motivo)
		pyplot.axis('equal')
		pyplot.title('Gastos Realizados')
		pyplot.savefig('media/graficas/pastel ' + str(self.pk) + '.png')
		pyplot.clf()

	def presupuestoinforme(self):
		return mark_safe('<a target="_blank" href="/informes/presupuesto/'+str(self.id)+'" class="Imprimir">Imprimir</a>')

	class Meta():
		db_table = 'presupuesto'
		verbose_name= 'Presupuesto'
		verbose_name_plural= 'Presupuestos'


TIPO_MOVIMIENTO=(
('Ingreso', 'Ingreso'),
('Egreso', 'Egreso'),
	)
class Movimiento(models.Model):
	fondos = models.ForeignKey(Presupuesto,on_delete=models.CASCADE, default=1)
	motivo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	tipo = models.CharField('Tipo de movimiento', max_length=8, choices=TIPO_MOVIMIENTO, default='Ingreso')
	cantidad = models.FloatField(default=0.00)
	fecha= models.DateField('Fecha', null=True, blank=True)
	descripcion= models.CharField('Descripcion', max_length=500, null=True, blank=True)
	evidencia = models.ImageField(upload_to='fotografias', max_length=500, null=True, blank=True)
		
	def __str__(self):
		return '%s %s' % (self.motivo, self.cantidad)


	def save(self, *args, **kwargs):

		super(Movimiento, self).save()
		self.fondos.save()

	class Meta():
		db_table = 'movimiento'
		verbose_name = 'Movimiento'
		verbose_name_plural = 'Movimientos'




