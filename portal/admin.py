from django.contrib import admin
from .models import Event, Registration
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'date', 'location']


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegisterAdmin)
