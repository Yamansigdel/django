from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import userForms
from service.models import Service
from news.models import News
from overview.models import Overview
from django.core.paginator import Paginator
from Contact.models import Contactenquire
from django.core.mail import send_mail,EmailMultiAlternatives

def homePage(request):
    # subject='Testing Mail'
    # from_email='yamansigdel999@gmail.com'
    # msg='<p>Welcome to <b>Yaman</b></p>'
    # to='yamunasigdel09@gmail.com'
    # msg=EmailMultiAlternatives(subject,msg,from_email,[to])
    # msg.content_subtype='html'
    # msg.send()



#     send_mail(
#     'Testing Mail',
#     'Here is the message',
#     'yamansigdel999@gmail.com',
#     ['yamunasigdel09@gmail.com'],
#     fail_silently=False,
# )
    
    newsData=News.objects.all()
    servicesData=Service.objects.all()
    paginator=Paginator(servicesData,1) #page lai paginate grna, 1 means 1 record in a page is there
    page_number=request.GET.get('page') #determine which page of Servicedata should be rendered, notmentioned--> default 
    servicesDatafinal=paginator.get_page(page_number) #retrieves page according to pg no.
    total_pages=servicesDatafinal.paginator.num_pages
    data={
        'servicesData':servicesDatafinal,
        'newsData':newsData,
        'last_page':total_pages,
        'totalpagelist':[n+1 for n in range(total_pages)]
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

    ovr=Overview.objects.all()
    dict={'ovr':ovr}

    return render(request,"overview.html",dict)

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
                if request.POST.get('num 1')=="":
                    return render(request,"evenodd.html", {'error':True})
                
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
            email=request.POST.get('Email')
            city=request.POST.get('city')
            n1=request.POST['first_name']
            n2=request.POST['last_name']
            fullname=n1+' '+ n2
            en=Contactenquire(email=email,city=city)
            en.save()
            data={
                'form':fn,
                'output':fullname
            }
            #url='/music/?fullname={}'.format(fullname)
            #return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)

