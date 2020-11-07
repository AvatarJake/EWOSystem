# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


# Create your models here.

class Event(models.Model):
    day = models.DateField(u'Dia del evento',)
    start_time = models.TimeField(u'Hora de Inicio',)
    end_time = models.TimeField(u'Hora de Finalizacion',)
    state=models.BooleanField('Pendiente', default=True)
    tipo_actividad=models.CharField('tipo actividad',max_length=30)
    notes = models.TextField(u'Descripcion', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agenda'


    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.tipo_actividad))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending hour must be after the starting hour')

        act = Event.objects.all()
        for e in act:
            if datetime.now().date() > e.day:
                e.state = False
                e.save()
        super(Event, self).clean()