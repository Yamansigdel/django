from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to myproject")

def course(request):
    return HttpResponse("Welcome to myproject1")

def courseDetails(request,courseid):
    return HttpResponse(courseid)