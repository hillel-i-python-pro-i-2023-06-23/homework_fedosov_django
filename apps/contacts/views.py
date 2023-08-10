from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.contacts.models import Contact


class ContactsListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone_number",
        # "is_auto_generated",
    )
    success_url = reverse_lazy('contacts:contacts_list')