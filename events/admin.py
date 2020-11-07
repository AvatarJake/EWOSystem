from __future__ import unicode_literals

from django.contrib import admin
from .models import Event
import datetime
import calendar
from django.urls import reverse
from django.utils.safestring import mark_safe
from .utils import EventCalendar

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['tipo_actividad','day', 'start_time', 'end_time','state', 'notes']
    change_list_template = 'admin/events/change_list.html'


    def changelist_view(self, request, extra_context=None):
        after_day = request.GET.get('day__gte', None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1) # encuentra el primer dia de el presente mes
        previous_month = previous_month - datetime.timedelta(days=1)  # regresa un solo dia
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)  # encuentra el primer dia del mes anterior

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  #encuentra el ultimo dia del presente mes
        next_month = next_month + datetime.timedelta(days=1)  # va hacia adelante un dia
        next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)   # encuentra el primer dia del siguiente mes

        extra_context['previous_month'] = reverse('admin:events_event_changelist') + '?day__gte=' + str(
            previous_month)
        extra_context['next_month'] = reverse('admin:events_event_changelist') + '?day__gte=' + str(next_month)

        cal = EventCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
        extra_context['calendar'] = mark_safe(html_calendar)
        return super(EventAdmin, self).changelist_view(request, extra_context)

admin.site.register(Event, EventAdmin)