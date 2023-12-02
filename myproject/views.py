from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import userForms
from service.models import Service
from news.models import News

def homePage(request):
    newsData=News.objects.all()
    servicesData=Service.objects.all()[:1]
    data={
        'servicesData':servicesData,
        'newsData':newsData
    }
    #print(len(newsData))
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
    return render(request,"index.html",data)


def overview(request):
    return render(request,"overview.html")

def calculator(request):
    c=''
    data={}
    try:
            if request.method=="POST":
                n1=eval(request.POST['num 1'])
                n2=eval(request.POST['num 2'])
                opr=request.POST['operator']
                if opr=='+':
                    c=n1+n2
                elif opr=='-':
                    c=n1-n2
                elif opr=='*':
                    c=n1*n2
                else:
                    c=n1/n2
            data={
                'n1':n1,
                'n2':n2,
                'opr':opr,
                'c':c
            }

                
    except:
        c="Error!!!"

    return render(request,"calculator.html",data)

def evenodd(request):
    c=" "
    data={}
    try:
            if request.method=="POST":
                n1=eval(request.POST['num 1'])
                if (n1%2) ==0:
                    c="Even Number"
                else:
                    c="Odd Number"

            data={
                'n1':n1,
                'c':c
            }

                
    except:
        c="Error!!!"

    return render(request,"evenodd.html",data)


def music(request):
    return render(request,"music.html")

def news(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetails
    }
    return render(request, "news.html",data)

def userForm(request):
    fullname=''
    fn=userForms()
    data={'form':fn}
    try:
        if request.method=="POST":
            n1=request.POST['first_name']
            n2=request.POST['last_name']
            fullname=n1+' '+ n2
            data={
                'form':fn,
                'output':fullname
            }
            #url='/music/?fullname={}'.format(fullname)
            #return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

