from django.db import models

# Create your models here.
class Application(models.Model):
    applicationId = models.IntegerField(unique=True,db_index=True,verbose_name="ID")
    applicationName = models.CharField(db_index=True, max_length=250,verbose_name="Navn")
    applicationSystem = models.CharField(db_index=True, blank=True, max_length=150, verbose_name="System")
    applicationDescription = models.TextField(verbose_name="Beskrivelse")
    applicationSystemOwner = models.CharField(db_index=True,max_length=250,verbose_name="Applikationsejer")
    applicationSystemOwnerContact = models.CharField(db_index=True, blank=True, max_length=250, verbose_name="Kontakt") 

class SupportDocumentation(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    applicationOneNoteId = models.CharField(max_length=250,default=" ",blank=True,null=True,verbose_name="OneNote ID")
