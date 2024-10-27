from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello!' to output"

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello')
