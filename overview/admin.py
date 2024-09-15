from django.contrib import admin
from overview.models import Overview

# Register your models here.
class OverviewAdmin(admin.ModelAdmin):
    list_display=('overview_title','overview_des')

admin.site.register(Overview,OverviewAdmin)