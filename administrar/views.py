from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from xhtml2pdf import pisa
from presupuesto.models import *
from actividades.models import *
from proyectos_sociales.models import *
from informes.models import *
from django.utils import timezone

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

class InicioView(TemplateView):
	template_name = "admin/inicio.html"

class PresupuestoPDF(View):


	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path


	def get(self, request, *args, **kwargs):
		año= Presupuesto.objects.get(pk=self.kwargs['pk'])
		year = año.pk
		template = get_template('informes/presupuesto.html')#define la ruta del html a ser pdf
		context = {
			'presupuesto': Presupuesto.objects.get(pk=self.kwargs['pk']),
			'ewo': {'name': 'Eyes Wide Open Ministries',
			'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),

			'pastel': '{}{}'.format(settings.MEDIA_URL, 'graficas/pastel ' + str(year) + '.png'),

			'fecha': timezone.now(),
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response

class ActividadPDF(View):


	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):

	
		template = get_template('informes/actividad.html')#define la ruta del html a ser pdf
		context = {
			'actividad': Actividad.objects.get(pk=self.kwargs['pk']),

			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),

			'fecha': timezone.now()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')

		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response
	
class ProyectoPDF(View):


	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):

	
		template = get_template('informes/proyecto.html')#define la ruta del html a ser pdf
		context = {
			'proyecto': Proyecto.objects.get(pk=self.kwargs['pk']),
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),

			'fecha': timezone.now()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response

class EventosPDF(View):


	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):

	
		template = get_template('informes/eventos.html')#define la ruta del html a ser pdf
		context = {
			'evento': Event.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'fecha': timezone.now()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response


class PastoresPDF(View):

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):

		template = get_template('informes/pastores.html')  # define la ruta del html a ser pdf
		context = {
			'pastores': Persona.objects.all(),
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'fecha': timezone.now()
		}  # dixionario de datos
		html = template.render(context)  # manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,  # crea el html
			link_callback=self.link_callback)  # llama la imagen

		return response


class EventosPendientesPDF(View):

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):

		template = get_template('informes/eventos_pendientes.html')  # define la ruta del html a ser pdf
		context = {
			'evento': Event.objects.all(),
			# accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'fecha': timezone.now()
		}  # dixionario de datos
		html = template.render(context)  # manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,  # crea el html
			link_callback=self.link_callback)  # llama la imagen

		return response

class EventosRealizadosPDF(View):

	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):

		template = get_template('informes/eventos_realizados.html')  # define la ruta del html a ser pdf
		context = {
			'evento': Event.objects.all(),
			# accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'fecha': timezone.now()
		}  # dixionario de datos
		html = template.render(context)  # manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,  # crea el html
			link_callback=self.link_callback)  # llama la imagen

		return response

class InformeProyectoRangoPDF(View):#PDF para la constancia de Estudios
	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):
		template = get_template('informes/proyectos_rango.html')#define la ruta del html a ser pdf
		context = {
			'proyecto': Proyecto.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'rango': ProyectoPorRango.objects.get(pk=self.kwargs['pk']),
			'grafica': '{}{}'.format(settings.MEDIA_URL, 'graficas/rangoproyecto.png'),
			'fecha': datetime.now().date()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response

class InformeTipoProyectoRangoPDF(View):#PDF para la constancia de Estudios
	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):
		template = get_template('informes/tipo_proyecto_rango.html')#define la ruta del html a ser pdf
		context = {
			'proyecto': Proyecto.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'rango': InformeTipoProyecto.objects.get(pk=self.kwargs['pk']),
			'grafica': '{}{}'.format(settings.MEDIA_URL, 'graficas/tipo_proyecto_rango.png'),
			'fecha': datetime.now().date()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response

class InformeActividadRangoPDF(View):#PDF para la constancia de Estudios
	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):
		template = get_template('informes/actividades_rango.html')#define la ruta del html a ser pdf
		context = {
			'proyecto': Actividad.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries', 'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'rango': ActividadPorRango.objects.get(pk=self.kwargs['pk']),
			'grafica': '{}{}'.format(settings.MEDIA_URL, 'graficas/rangoactividad.png'),
			'fecha': datetime.now().date()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(

			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response

class InformePresupuestoRangoPDF(View):#PDF para la constancia de Estudios
	def link_callback(self, uri, rel):
		sUrl = settings.STATIC_URL  # Typically /static/
		sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
		mUrl = settings.MEDIA_URL  # Typically /static/media/
		mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

		# convert URIs to absolute system paths
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri  # handle absolute uri (ie: http://some.tld/foo.png)

		# make sure that file exists
		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
			)
		return path

	def get(self, request, *args, **kwargs):
		template = get_template('informes/presupuesto_rango.html')#define la ruta del html a ser pdf
		context = {
			'presupuesto': Movimiento.objects.all(),#accede a los datos de la base, con pk=self.kwargs['pk'] acede al id que le enviamos
			'ewo': {'name': 'Eyes Wide Open Ministries',
			'dir': 'El Morral, Chiquimula'},
			'icon': '{}{}'.format(settings.MEDIA_URL, 'sistema/logoinforme.png'),
			'rango': PresupuestoPorRango.objects.get(pk=self.kwargs['pk']),
			'grafica': '{}{}'.format(settings.MEDIA_URL, 'graficas/rangopresupuesto.png'),
			'fecha': datetime.now().date()
		}#dixionario de datos
		html = template.render(context)#manda el dixionario de datos
		response = HttpResponse(content_type='application/pdf')
		pisaStatus = pisa.CreatePDF(
			html, dest=response,#crea el html
			link_callback=self.link_callback)#llama la imagen

		return response