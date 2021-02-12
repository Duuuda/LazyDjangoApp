from django.core.management.base import BaseCommand
from os import system


class Command(BaseCommand):
    help = 'This function prepares and launches Django without user intervention'

    def handle(self, *args, **options):
        system('python manage.py collectstatic --no-input')
        system('python manage.py remigrate')
        system('python manage.py checkdefaultuser')
        system('python manage.py runserver')
