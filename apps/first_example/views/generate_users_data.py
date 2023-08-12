from django.shortcuts import render
from apps.first_example.services.generate_users_data import generate_users_data


def generate_users_data_view(
    request,
    amount: int = 5,
):
    users = generate_users_data(amount=amount)
    return render(
        request=request,
        template_name="first_example/generate_users_data.html",
        context=dict(
            users=users,
            title="Users",
        ),
    )
