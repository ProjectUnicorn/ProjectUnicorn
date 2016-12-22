from django.db import models

# Create your models here.
class Application(models.Model):
    applicationId = models.IntegerField(unique=True,db_index=True,verbose_name="ID")
    applicationName = models.CharField(db_index=True, max_length=250,verbose_name="Navn")
    applicationDescription = models.TextField(verbose_name="Beskrivelse")
    applicationSystemOwner = models.CharField(db_index=True,max_length=250,verbose_name="Applikationsejer")
    applicationOneNoteId = models.CharField(max_length=250,default="",blank=True,null=True,verbose_name="OneNote ID")
