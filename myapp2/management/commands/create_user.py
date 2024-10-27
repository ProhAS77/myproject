from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        #user = User(name='John', email='111@mail.ru', password='111', age=25)
        #user = User(name='NEO', email='222@mail.ru', password='222', age=22)
        user = User(name='Jack', email='333@mail.ru', password='333', age=33)
        user.save()
        self.stdout.write(f'{user}')
