from django.http import HttpResponse


def index(request):
    return HttpResponse(f"<h1>Welcome  to Django!</h1>")

def welcome(request, name):
    return HttpResponse(f"""<html><head><style>body{{background-color:green;color:red;font-family:Arial, sans-serif;}}</style></head><body><h1>Welcome {name} to Django!</h1></body></html>""")