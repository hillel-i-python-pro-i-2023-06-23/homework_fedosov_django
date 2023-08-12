from collections.abc import Iterator

from apps.contacts.models import Contact
from faker import Faker

faker = Faker()


def generate_contact() -> Contact:
    return Contact(
        name=faker.first_name(),
        phone_number=faker.phone_number(),
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
