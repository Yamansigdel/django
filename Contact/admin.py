from django.contrib import admin

from Contact.models import Contactenquire

class Contactadmin(admin.ModelAdmin):
    list_display=('email','city')

admin.site.register(Contactenquire,Contactadmin)
