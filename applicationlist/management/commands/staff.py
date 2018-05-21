# -*- coding: utf-8 -*-
from django.core.management import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
  # Show this when the user types help
  help = "Add a user to the staff group (needed to edit in the applicationlist)"

  def add_arguments(self, parser):
      parser.add_argument('user', type=str)

      # optional arguments
      parser.add_argument(
          '-r',
          action='store_true',
          dest='remove',
          help='Removes user from staff group'
      )
      parser.add_argument(
          '-a',
          action='store_true',
          dest='add',
          help='Adds a user to staff group'
      )

  def handle(self, *args, **options):
          try:
              user = User.objects.get(username=options['user'])
          except User.DoesNotExist:
              raise CommandError('User does not exist.')
          if user.is_staff:
            self.stdout.write('%s is in staff' % user.username)
          else:
              self.stdout.write('%s is not in staff' % user.username)

          if options['remove'] and user.is_staff:
              user.is_staff = False
              user.save()
              self.stdout.write(self.style.SUCCESS('Removed %s from staff group.' % user.username))

          if options['add'] and not user.is_staff:
              user.is_staff = True
              user.save()
              self.stdout.write(self.style.SUCCESS('Added %s to staff group.' % user.username))
