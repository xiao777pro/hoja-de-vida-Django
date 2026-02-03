import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crea un superusuario si no existe usando variables de entorno'

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        
        if not password:
            self.stdout.write(self.style.ERROR('Error: DJANGO_SUPERUSER_PASSWORD no está definida'))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'El usuario "{username}" ya existe'))
        else:
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado exitosamente'))
