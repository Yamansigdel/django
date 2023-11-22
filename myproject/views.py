from django.http import HttpResponse
from django.shortcuts import render,redirect

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
    if request.method=="GET":
        fullname=request.GET['fullname']
    return render(request,"music.html",{'fullname':fullname})

def userForm(request):
    fullname=''
    try:
        if request.method=="POST":
            n1=request.POST['first_name']
            n2=request.POST['last_name']
            fullname=n1+' '+ n2
            url='/music/?fullname={}'.format(fullname)
            return redirect(url)
    except:
        pass
    return render(request,"userform.html",{'output':fullname})
