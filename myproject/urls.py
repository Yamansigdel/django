"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myproject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('admin/', admin.site.urls,name="admin"),
    path('overview/',views.overview,name="overview"),
    path('music/',views.music,name="music"),
    path('news/<slug>',views.news),
    path('userform/',views.userForm,name="form"),
    path('calculator/', views.calculator,name="calculator"),
    path('evenodd/', views.evenodd),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#admin username: admin
#admin pass: yaman101