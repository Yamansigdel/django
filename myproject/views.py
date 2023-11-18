from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Welcome to myproject")

def course(request):
    return HttpResponse("Welcome to myproject1")

def courseDetails(request,courseid):
    return HttpResponse(courseid)