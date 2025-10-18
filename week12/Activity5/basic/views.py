from django.http import HttpResponse


def index(request):
    return HttpResponse(f"<h1>Welcome  to Django!</h1>")

def welcome(request, name):
    return HttpResponse(f"<h1>Welcome {name} to Django!</h1>")