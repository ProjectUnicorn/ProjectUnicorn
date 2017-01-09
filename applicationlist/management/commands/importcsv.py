# -*- coding: utf-8 -*-
from django.core.management import BaseCommand

import csv
import applicationlist

class Command(BaseCommand):
  # Show this when the user types help
  help = "Import data from Systemliste.csv"

  def handle(self, *args, **options):
    f = open('Systemliste.csv')
    c = csv.DictReader(f, delimiter=';', quotechar='"')
    for row in c:
      formaal = row["Formaal"]
      ejer    = row["Systemejer"]
      navn    = row["AAU Navn"]
      app_id  = int(row["ID"])
      a = applicationlist.models.Application(applicationId=app_id, applicationName=navn, applicationDescription=formaal, applicationSystemOwner=ejer, applicationOneNoteId="")
      a.save()
