from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Como estas')