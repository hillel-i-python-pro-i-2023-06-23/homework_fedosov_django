from django.http import HttpResponse
from .services.generate_emails import show_emails

def homework(request):
    return HttpResponse(f"Hello, Alex!\nThis is my homework:<ol>{show_emails()}</ol>")


