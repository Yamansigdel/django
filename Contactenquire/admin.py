from django.contrib import admin
from Contactenquire.models import Contact

class Contactadmin(admin.ModelAdmin):
    list_display=('contact_title','contact_desc')

admin.site.register(Contact,Contactadmin)