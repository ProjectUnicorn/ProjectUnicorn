# -*- coding: utf-8 -*-
from django.core.management import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
  # Show this when the user types help
  help = "Add a user to the super group (needed to admin site login)"

  def add_arguments(self, parser):
      parser.add_argument('user', type=str)

      # optional arguments
      parser.add_argument(
          '-r',
          action='store_true',
          dest='remove',
          help='Removes user from super group'
      )
      parser.add_argument(
          '-a',
          action='store_true',
          dest='add',
          help='Adds a user to super group'
      )

  def handle(self, *args, **options):
          try:
              user = User.objects.get(username=options['user'])
          except User.DoesNotExist:
              raise CommandError('User does not exist.')
          if user.is_superuser:
            self.stdout.write('%s is in super' % user.username)
          else:
              self.stdout.write('%s is not in super' % user.username)

          if options['remove'] and user.is_superuser:
              user.is_superuser = False
              user.save()
              self.stdout.write(self.style.SUCCESS('Removed %s from super group.' % user.username))

          if options['add'] and not user.is_superuser:
              user.is_superuser = True
              user.is_staff = True
              user.save()
              self.stdout.write(self.style.SUCCESS('Added %s to super group.' % user.username))
