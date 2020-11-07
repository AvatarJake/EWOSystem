# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
GENERO=(
	('M', 'Masculino'),
	('F', 'Femenino'),
	)

class Comun(models.Model):
	"""docstring for ClassName"""
	nombres = models.CharField('nombres', max_length=50)
	apellidos = models.CharField('apellidos', max_length=50)
	genero= models.CharField('genero', max_length=1, choices=GENERO, default='M')
	telefono= models.PositiveIntegerField('telefono')
	activo = models.BooleanField(default=True)


	def __str__(self):
		return "%s %s" % (self.nombres,  self.apellidos)
		
		class Meta():
			abstract = True

