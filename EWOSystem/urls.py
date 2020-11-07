"""EWOSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from administrar.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('admin/', admin.site.urls),
    path('informes/presupuesto/<int:pk>', login_required(PresupuestoPDF.as_view()), name='informe'),
    path('informes/actividad/<int:pk>', login_required(ActividadPDF.as_view()), name='informeactividad'),
    path('informes/proyecto/<int:pk>', login_required(ProyectoPDF.as_view()), name='informeproyecto'),
    path('informes/eventos/', login_required(EventosPDF.as_view()), name='informeeventos'),
    path('informes/eventos_pendientes/', login_required(EventosPendientesPDF.as_view()), name='eventospendientes'),
    path('informes/eventos_realizados/', login_required(EventosRealizadosPDF.as_view()), name='eventosrealizados'),
    path('informes/pastores/', login_required(PastoresPDF.as_view()), name='informepastores'),
    path('informes/proyectos_rango/<int:pk>', login_required(InformeProyectoRangoPDF.as_view()), name='proyecto_por_rango'),
    path('informes/actividades_rango/<int:pk>', login_required(InformeActividadRangoPDF.as_view()), name='actividad_por_rango'),
    path('informes/presupuesto_rango/<int:pk>', login_required(InformePresupuestoRangoPDF.as_view()), name='presupuesto_por_rango'),
    path('informes/tipo_proyecto_rango/<int:pk>', login_required(InformeTipoProyectoRangoPDF.as_view()), name='tipo_proyecto_rango'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
