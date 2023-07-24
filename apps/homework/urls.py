from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
    path("run/", views.homework, name="homework"),

]
