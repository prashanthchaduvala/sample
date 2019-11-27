"""online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Admin,name='main'),
    path('log/',views.login,name='login'),
    path('merchant/',views.merchant,name='merchant'),
    path('add/',views.addmerchant,name='add'),
    path('save/',views.save,name="save"),
    path('saves/',views.saves,name='saves'),
    #path('delete/',views.delete,name='delete'),
    path('deleteid/',views.deleteid,name='deleteid'),

#    path('p_add/',views.addsales,name='p_add'),
   # path('p_adds/',views.p_save,name='p_save'),
   # path('p_saves/',views.p_savess,name='p_saves'),

    path('merchantlog/<str:username>/<str:password>/',views.merchantlog.as_view()),
    #path('resetpassword/<str:gmailpassword>/',views.resetpassword.as_view()),
    path('addproduct/',views.merchantlog.as_view()),
    #path('resetpassword/<str:gmailpassword>/', views.resetpassword.as_view())

]

