from django.db import models
from comun.models import Comun
from .models import *
from django.utils.safestring import mark_safe


# Create your models here.
ORIGEN_OPCIONES=(
    ('I', 'Internacional'),
    ('L', 'Local'),
    )
class Lugar(models.Model):
    nombre = models.CharField('nombre', max_length=50, unique=True)
    origen = models.CharField ('origen', max_length=1, choices=ORIGEN_OPCIONES, default='L')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nombre,' ')

    def clean(self): # limpiar los campos antes de insertar o actualizar
        super(Lugar, self).clean()


    def save(self, **kwargs): # Guardar los campos despeus de insertar o actualizar

        if self.activo:
            self.nombre.upper()

        else:
            self.nombre = self.nombre.lower()

        super(Lugar, self).save()

    class Meta():
        db_table = 'lugar'
        verbose_name= 'Lugar'
        verbose_name_plural= 'Lugares'

class Cargo(models.Model):
    """docstring for ClassName"""
    nombre = models.CharField('Puesto', max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nombre,' ')

    def clean(self): # BEFORE INSERT OR UPDATE
        super(Cargo, self).clean()


    def save(self, **kwargs): # AFTER INSERT OR UPDATE

        if self.activo:
            self.nombre.upper()

        else:
            self.nombre = self.nombre.lower()

        super(Cargo, self).save()

    class Meta():
        db_table = 'cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

class Iglesia(models.Model):
    nombre = models.CharField('nombre', max_length=50, null=True)
    lugar = models.ForeignKey(Lugar,on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.lugar)

    def clean(self): # BEFORE INSERT OR UPDATE
        super(Iglesia, self).clean()


    def save(self, **kwargs): # AFTER INSERT OR UPDATE

        if self.activo:
            self.nombre.upper()

        else:
            self.nombre = self.nombre.lower()

        super(Iglesia, self).save()

    class Meta():
        db_table = 'iglesia'
        verbose_name= 'Iglesia'
        verbose_name_plural= 'Iglesias'

class Miembro(Comun):
    cargo= models.ForeignKey(Cargo, on_delete=models.CASCADE)
    sueldo = models.FloatField(default=0)
    lugar= models.ForeignKey(Lugar,on_delete=models.CASCADE)
    email= models.EmailField('correo', null=True, blank='True')

    def clean(self): # Limpiar antes de insertar o actualizar
        super(Miembro, self).clean()


    def save(self, **kwargs): # Activar o inactivar un miembro

        if self.activo:
            self.nombres = self.nombres.upper()
            self.apellidos = self.apellidos.upper()
        else:
            self.nombres = self.nombres.lower()
            self.apellidos = self.apellidos.lower()

        super(Miembro, self).save()

    class Meta():
        db_table = 'miembro'
        verbose_name= 'Miembro'
        verbose_name_plural= 'Miembros'

class TipoPersona(models.Model):
    tipo= models.CharField('Tipo de Persona', max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '%s ' % (self.tipo,)

    def clean(self): # limpiar los campos antes de insertar o actualizar
        super(TipoPersona, self).clean()

    def save(self, **kwargs): # Guardar los campos despeus de insertar o actualizar

        if self.activo:
            self.tipo.upper()

        else:
            self.tipo = self.tipo.lower()

        super(TipoPersona, self).save()

    class Meta():
        db_table = 'tipopersona'
        verbose_name = 'TipoPersona'
        verbose_name_plural = 'TipoPersonas'

class Persona(Comun):
    tipo= models.ForeignKey(TipoPersona,on_delete=models.CASCADE)
    nombre_Iglesia = models.ForeignKey(Iglesia,on_delete=models.CASCADE)
    lugar= models.ForeignKey(Lugar,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.nombres, self.apellidos, self.tipo, self.lugar)

    def clean(self): # Limpiar antes de insertar o actualizar
        super(Persona, self).clean()

    def save(self, **kwargs): # Activar o inactivar una persona

        if self.activo:
            self.nombres = self.nombres.upper()
            self.apellidos = self.apellidos.upper()
        else:
            self.nombres = self.nombres.lower()
            self.apellidos = self.apellidos.lower()

        super(Persona, self).save()

    class Meta():
        db_table = 'persona'
        verbose_name= 'Persona'
        verbose_name_plural= 'Personas'
