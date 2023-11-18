from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'Welcome to my project',
        'clist':['PHP','JAVA','Python'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'pradeep','phone':9840031339},
            {'name':'testing','phone':9840031339},
        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to myproject")

def course(request):
    return HttpResponse("Welcome to myproject1")

def courseDetails(request,courseid):
    return HttpResponse(courseid)