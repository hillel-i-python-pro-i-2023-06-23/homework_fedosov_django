import logging

from apps.contacts.models import Contact
from apps.contacts.services.generate_humans import generate_contacts


def generate_and_save_contacts(amount:int):
    logger = logging.getLogger('django')
    queryset = Contact.objects.all()
    logger.info(f"Current amount of contacts before: {queryset.count()}")

    for human in generate_contacts(amount=amount):
        human.is_auto_generated = True
        human.save()

    logger.info(f"Current amount of contacts after: {queryset.count()}")
