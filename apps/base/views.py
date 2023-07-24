from django.http import HttpResponse



def home_page(request):
    return HttpResponse(f"Hallo homework!")
