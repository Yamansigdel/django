from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page'
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to myproject")

def course(request):
    return HttpResponse("Welcome to myproject1")

def courseDetails(request,courseid):
    return HttpResponse(courseid)