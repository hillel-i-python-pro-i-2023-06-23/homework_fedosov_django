

from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView

from apps.contacts.forms import GenerateForm, ContactSpecialEditForm
from apps.contacts.models import Contact
from apps.contacts.services.delete_contacts import delete_contacts
from apps.contacts.services.generate_and_save_contacts import generate_and_save_contacts
from apps.contacts.services.generate_humans import generate_contacts


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

class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "name",
        "phone_number",
        # "is_auto_generated",
    )

    def get_success_url(self):
        return reverse_lazy("contacts:contacts_update", kwargs=dict(pk=self.kwargs["pk"]))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:contacts_list')



def generate_contacts_view__raw_form(request):
    if request.method == 'POST':
        amount = int(request.POST["amount"])

        generate_and_save_contacts(amount=amount)

    return render(
        request=request,
        template_name='contacts/contacts_generate__raw_form.html',
        context=dict(
            contacts_list=Contact.objects.all(),
        )
    )


def generate_contacts_view(request):
    if request.method == 'POST':

        form = GenerateForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']

            generate_and_save_contacts(amount=amount)
    else:
        form = GenerateForm()

    return render(
        request=request,
        template_name='contacts/contacts_generate.html',
        context=dict(
            contacts_list=Contact.objects.all(),
            form=form,


        )
    )



class ContactSpecialEdit(FormView):
    model = Contact
    form_class = ContactSpecialEditForm
    template_name = "contacts/contact_form.html"

    def get_success_url(self):
        return reverse_lazy("contacts:contacts_special_edit", kwargs=dict(pk=self.kwargs["pk"]))


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = Contact.objects.get(pk=self.kwargs["pk"])
        return kwargs


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def delete_contacts_view(request):
    delete_contacts()

    return redirect(reverse_lazy("contacts:contacts_list"))