from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contacts_list"),
    path("create/", views.ContactCreateView.as_view(), name="contacts_create"),
]
