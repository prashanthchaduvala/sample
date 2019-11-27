from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .models import Savemodel,Merchantmodel
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
#from django.utils.decorators import method_decorator
from .forms import SavemodelForm
import random
import json
# Create your views here.

# def session(request):
#     request.session['sname']='user'
#     request.session['semail']='email'
#     return HttpResponse('session is set')
# def getsession(request):
#     username=request.session['sname']
#     password=request.session['semail']
#     return HttpResponse(username+""+password)
def Admin(request):
    #uname=request.POST.get('user')
    #password=request.POST.get('pass')
   # if uname == "admin" and password == "admin":
        return render(request,"index.html")
    #else:
     #   return render(request,'index.html')


def login(request):
    username=request.POST['user']
    password=request.POST['pass']
    if username == "admin" and password == "admin":
        return render(request,"welcome.html")
    else:
        return render(request,"index.html")


def merchant(request):
    return render(request,'merchant.html')


def addmerchant(request):
    #id=random.randrange(11,99)
    try:
        idno=Savemodel.objects.all()[::-1][0].id
        idno+=1
    except IndexError:
        idno=10
    paword=random.randrange(111111,999999)
    return render(request,'add.html',{'id':idno,"pas":paword})
    #"pas":pas


def save(request):
    id=request.POST['id']
    name=request.POST['name']
    contact=request.POST['contact']
    email=request.POST['email']
    password=request.POST['pass']
    Savemodel(id=id,name=name,contact=contact,email=email,password=password).save()
    return render(request,'save.html',{'message':'data saved'})

def saves(request):
    rm=Savemodel.objects.all()
    return render(request,'save.html',{'data':rm})


def delete(request):
    return render(request,'delete.html')


def deleteid(request):
    id=request.GET.get('id')
    Savemodel.objects.filter(id=id).delete()
    return render(request,'save.html',{"message":'delete sucessfully'})



class merchantlog(View):
    def get(self,request,username,password):
        try:
            res = Savemodel.objects.get(email=username,password=password)
        except:
            data = json.dumps({'message':'invalid '})
            return HttpResponse(data,content_type='application/json',status=400)
        else:
            messa=json.dumps({"messssage":'invalid'})
            return HttpResponse(messa,content_type='application/json',status=200)


# class resetpassword(View):
#     def put(self,request,gmailpassword):
#         try:
#             res=Savemodel.objects.get(password=gmailpassword)
#         except:
#             data=json.dumps({'message':'invalid'})
#             return HttpResponse(data,content_type='application/json',status=400)
#         else:
#             messa=json.dumps({'messsage':'invalid'})
#             return HttpResponse(messa,content_type='application/json',status=200)


'''@method_decorator(csrf_exempt,name="dispatch")
class resetpassword(View):
    def put(self,request,gmailpassword):
        try:
            old_data = Savemodel.objects.get(password=gmailpassword)
        except Savemodel.DoesNotExist:
            json_mess = json.dumps({"error_message":"Given password is Invalid"})
            return HttpResponse(json_mess,content_type="application/json")
        else:
            # old_data is in object Format but we need in dict format
            # Converting object to dict
            old_data_dict ={"email":old_data.email,}

            data = request.body
            new_data = json.loads(data)

            # updating old_data with new_data
            old_data_dict.update(new_data)

            ef = SavemodelForm(old_data_dict)

            if ef.is_valid():
                ef.update()
                json_mess = json.dumps({"message": "password updated"})
                return HttpResponse(json_mess, content_type="application/json")
            if ef.errors:
                json_mess = json.dumps(ef.errors)
                return HttpResponse(json_mess, content_type="application/json")'''





'''def addsales(request):
    return render(request,'p_add.html')

def p_save(request):
    p_id=request.POST['p_id']
    p_name=request.POST['p_name']
    p_price=request.POST['p_price']
    p_qty=request.POST['p_qty']
    Merchantmodel(p_no=p_id,p_name=p_name,p_price=p_price,p_qty=p_qty).save()
    return render(request,'p_save.html',{'message':'data saved'})



def p_savess(request):
    sm=Merchantmodel.objects.all()
    return render(request,'p_save.html',{'data':sm})'''


