from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default=0,
        )
    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    modified_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.name} {self.phone_number}"

    __repr__ = __str__
