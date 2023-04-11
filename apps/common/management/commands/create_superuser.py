from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates a superuser account with a specified username.'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The desired username of the new superuser.')

    def handle(self, *args, **options):
        USER = get_user_model()

        username = options['username']
        password = "admin"

        USER.objects.create_superuser(
            username=username,
            email="admin@example.com",
            password=password
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Superuser created successfully.😊\nPassword: {password}"
            )
        )
