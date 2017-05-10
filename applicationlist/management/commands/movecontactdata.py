from django.core.management import BaseCommand
from applicationlist.models import *

import applicationlist

class Command(BaseCommand):
  # Print this when user request help
  help = "Moves data from the applicationSystemOwner column to the applicationSystemOwnerContact column, and the other way around."

  def handle(self, *args, **options):
    all_objects_from_database = Application.objects.all()
    delimiter_contact = "/"

    for row in all_objects_from_database:
      if delimiter_contact in row.applicationSystemOwner: # Moves email from owner to contact
        data_to_be_moved = row.applicationSystemOwner.split(delimiter_contact)[1]
        data_to_stay = row.applicationSystemOwner.split(delimiter_contact)[0]
        row.applicationSystemOwnerContact = data_to_be_moved
        row.applicationSystemOwner = data_to_stay

        print("Moved: " + data_to_be_moved + " to contact column.")

      row.save()
