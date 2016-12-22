from django.contrib import admin
from .models import *
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicationId','applicationName','applicationDescription','applicationSystemOwner','applicationOneNoteId')


admin.site.register(Application,ApplicationAdmin)