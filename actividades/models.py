from datetime import datetime

from django.db import models
from .models import *
from administrar.models import Lugar
from administrar.models import Persona
from administrar.models import Miembro
from events.models import Event
from django.utils.safestring import mark_safe
import smtplib
from email.mime.multipart import MIMEMultipart
from administrar.models import *
from email.mime.text import MIMEText



class Tipo_Actividad(models.Model):
	nombre= models.CharField('Nombre de la actividad', max_length=50, unique=True)
	descripcion = models.TextField('Descripcion', max_length=1000, null=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s %s' % (self.nombre, ' ')

	def clean(self): # limpiar los campos antes de insertar o actualizar
		super(Tipo_Actividad, self).clean()


	def save(self, **kwargs): # Guardar los campos despeus de insertar o actualizar

		if self.activo:
			self.nombre.upper()
			
		else:
			self.nombre = self.nombre.lower()
			
		super(Tipo_Actividad, self).save()
		
	class Meta():
		db_table = 'tipo_actividad'
		verbose_name = 'Tipo actividad'
		verbose_name_plural = 'Tipo actividades'

class Actividad(models.Model):
	"""docstring for Actividad"""
	tipo_actividad=models.ForeignKey(Tipo_Actividad,on_delete=models.CASCADE)
	lugar= models.ForeignKey(Lugar,on_delete=models.CASCADE)
	fecha=models.DateField('Fecha de Actividad', null=True, blank=True)
	hora_inicio=models.TimeField('Hora de inicio', blank=True, null=True)
	hora_fin=models.TimeField('Hora de finalizacion', blank=True, null=True)
	descripcion=models.TextField('Descripcion', max_length=1000, blank=True, null=True)
	imagenes=models.ImageField(upload_to='fotografias', max_length=None, null=True, blank= True)
	participantes=models.ManyToManyField(Persona)

	def __str__(self):
		return '%s %s' % (self.tipo_actividad,' ')

	def clean(self):
		
		super(Actividad, self).clean()


	def save(self, *args, **kwargs):
		event = Event.objects.create(
			day=self.fecha,
			start_time=self.hora_inicio,
			end_time=self.hora_fin,
			tipo_actividad=self.tipo_actividad,
			notes=self.descripcion),
		super(Actividad, self).save(*args,**kwargs)

		emails = Miembro.objects.all()
		destino = []

		for e in emails:
			destino.append(e.email)
		print(destino)

		msg = MIMEMultipart()
		direccionenvio = 'ewosystem@gmail.com'
		msg['From'] = direccionenvio
		msg['To'] = ",".join(destino)
		msg['Subject'] = 'Nuevo evento Programado'

		html_body = f'''
				<html>
					<head></head>
					<body>
					<h1>Hola, se ha programado un nuevo evento</h1>
					<p>Tipo de Proyecto: {self.tipo_actividad}</p>
					<p>Lugar: {self.lugar}</p>
					<p>Fecha: {self.fecha}</p>
					<p>Hora de Inicio: {self.hora_inicio}</p><br><br>
					<p> Gracias por formar parte de nuestro equipo, que tengas un bendecido dia!!</p>
					</body>
				</html>
						'''
		msg.attach(MIMEText(html_body, 'html'))
		smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
		smtp_server.ehlo()
		smtp_server.starttls()
		smtp_server.login('ewosystem@gmail.com', 'jake09101989')
		text = msg.as_string()
		smtp_server.sendmail(direccionenvio, destino, text)
		smtp_server.quit()

		print("el correo fue enviado!")


	def actividadinforme(self):
		return mark_safe('<a target="_blank" href="/informes/actividad/'+str(self.id)+'" class="Imprimir">Imprimir</a>')


	class Meta:
			db_table = 'actividad'
			verbose_name = 'Actividad'
			verbose_name_plural = 'Actividades'


class Responsable(models.Model):
	"""docstring for ActividadParticipantes"""
	actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
	responsable= models.ForeignKey(Miembro, on_delete=models.CASCADE)
	trabajo = models.CharField('trabajo', max_length=30, blank=True, null=True)
	Descripcion = models.CharField('Descripcion', max_length=1000, null=True, blank=True)
	imagenes = models.ImageField(upload_to='fotografias', max_length=500, null=True, blank=True)


	class Meta:
			db_table = 'responsable'
			verbose_name = 'Responsable'
			verbose_name_plural = 'Responsables'

