from django.contrib import admin
from .models import *
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicationId','applicationName', 'applicationSystem','applicationSystemOwner', 'applicationSystemOwnerContact', 'applicationDescription')


admin.site.register(Application,ApplicationAdmin)
