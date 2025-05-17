# apartments/management/commands/create_test_data.py

from django.core.management.base import BaseCommand
from apps.apartments.factories import UserFactory, ApartmentFactory


class Command(BaseCommand):
    help = "Створити тестових користувачів та квартири"

    def handle(self, *args, **kwargs):
        users = UserFactory.create_batch(5)
        self.stdout.write("Створено 5 користувачів")

        for user in users:
            ApartmentFactory.create_batch(3, owner=user)
        self.stdout.write("Кожен користувач отримав по 3 квартири")
