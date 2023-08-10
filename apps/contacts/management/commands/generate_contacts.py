import logging

from django.core.management import BaseCommand

from apps.contacts.models import Contact
from apps.contacts.services.generate_humans import generate_contacts


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

        logger = logging.getLogger('django')
        queryset = Contact.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        for human in generate_contacts(amount=amount):
            human.is_auto_generated = True
            human.save()

        logger.info(f"Current amount of contacts after: {queryset.count()}")
