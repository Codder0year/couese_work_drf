from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email='admin1@localhost',
            first_name='admin',
            password='Blev2011',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password('Blev2011')
        user.save()