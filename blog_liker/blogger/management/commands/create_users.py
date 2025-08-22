from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Populate the User model with fake data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=10, help="Number of users to create"
        )

    def handle(self, *args, **kwargs):
        faker = Faker()
        count = kwargs["count"]
        created = 0
        for _ in range(count):
            first_name = faker.first_name()
            last_name = faker.last_name()
            email = faker.email()

            # Ensure username is unique
            User = get_user_model()
            while User.objects.filter(email=email).exists():
                email = faker.email()

            password = "password123"  # Or generate a random password if preferred

            user = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            self.stdout.write(f"Created user: {user.email}")
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully created {created} users."))
