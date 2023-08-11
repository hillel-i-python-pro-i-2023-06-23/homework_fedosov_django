from django.core.management import BaseCommand

from apps.contacts.services.generate_and_save_contacts import generate_and_save_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help='How many humans you want to generate ?',
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        generate_and_save_contacts(amount=amount)


