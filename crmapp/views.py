from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth
# Create your views here.
def crmhome(request):
    return render(request,'crmhome.html')

def crmnavv(request):
    return render(request,'crmnavv.html')

def crmsignin(request):
    return render(request,'crmsignin.html')

def crmregister(request):
    return render(request,'crmregister.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
                messages.info(request,'Username exists')
                return redirect('crmregister')
        elif User.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect('crmregister')
        
        else :
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect('crmsignin')
    
def signinpage(request):
    if request.method=='POST':
        uname=request.POST['user']
        password=request.POST['pas']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('crmloginpage')
        else:
            messages.info(request,'Invalid Username or password')
            return redirect('crmsignin')
        
def crmcontact(request):
    return render(request,'crmcontact.html')

def log_out(request):
    auth.logout(request)
    return redirect('crmhome')

def crmloginpage(request):
     currentuser=request.user.username
     
     return render(request,'crmloginpage.html',{'currentuser':currentuser})
     
