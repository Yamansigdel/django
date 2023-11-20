from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # data={
    #     'title':'Home Page',
    #     'bdata':'Welcome to my project',
    #     'clist':['PHP','JAVA','Python'],
    #     'numbers':[10,20,30,40,50],
    #     'student_details':[
    #         {'name':'pradeep','phone':9840031339},
    #         {'name':'testing','phone':9840031339},
    #     ]
    # }
    return render(request,"index.html")

def overview(request):
    return render(request,"overview.html")

def music(request):
    return render(request,"music.html")

def userForm(request):
    fullname=''
    try:
        n1=request.GET['first_name']
        n2=request.GET['last_name']
        fullname=n1+' '+ n2
    except:
        pass
    return render(request,"userform.html",{'output':fullname})
