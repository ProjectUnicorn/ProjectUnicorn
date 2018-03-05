from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class ClassificationColor(models.Model):
    color = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.color

class Classification(models.Model):
    name = models.CharField(db_index=True, max_length=100, blank=True, verbose_name="Klassifikation")
    color = models.ForeignKey(ClassificationColor, verbose_name="Farve")

    def __str__(self):
        return self.name

class Application(models.Model):
    applicationId = models.IntegerField(unique=True,db_index=True,verbose_name="ID")
    applicationName = models.CharField(db_index=True, max_length=250,verbose_name="Service")
    applicationSystem = models.CharField(db_index=True, blank=True, max_length=150, verbose_name="System")
    applicationDescription = models.TextField(verbose_name="Beskrivelse")
    applicationSystemOwner = models.CharField(db_index=True,max_length=250,verbose_name="Ejer")
    applicationSystemOwnerContact = models.CharField(db_index=True, blank=True, max_length=250, verbose_name="Kontakt")
    applicationRiskEvaluation = models.URLField(blank=True, max_length=255, verbose_name="Risikovurdering")
    applicationClassification = models.ForeignKey(Classification, null=True, on_delete=models.CASCADE, verbose_name="Klassifikation")
    applicationDataDeal = models.URLField(blank=True, max_length=255, verbose_name="Data aftale")
    applicationContainsPersonData = models.BooleanField(default=False, verbose_name="Persondata")

    def datadeal_url(self):
        return '<a href="{}">{}</a>'.format(self.applicationDataDeal, "link")

class SupportDocumentation(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    applicationOneNoteId = models.CharField(max_length=250,default=" ",blank=True,null=True,verbose_name="OneNote ID")
