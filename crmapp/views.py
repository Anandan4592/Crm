from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
import json
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

def crmpricing(request):
    return render(request,'crmpricing.html')

def log_out(request):
    auth.logout(request)
    return redirect('crmhome')

def crmusernav(request):
    return render(request,'crmusernav.html')

def crmloginpage(request):
     currentuser=request.user.username
     
     return render(request,'crmloginpage.html',{'currentuser':currentuser})

def crmarchive(request):
    currentuser=request.user.username
    return render(request,'crmarchive.html',{'currentuser':currentuser})

def archive(request):
    if 'card' in request.GET:
        # Retrieve the encoded card data from the URL parameters
        encoded_card_data = request.GET['card']
        # Decode the card data from URL encoding
        card_data = json.loads(encoded_card_data)
        # Render the archive page with the card data
        return render(request, 'crmarchive.html', {'card_data': card_data})
    else:
        # If there is no card data in the URL parameters, render the archive page without any data
        return render(request, 'crmarchive.html')
     
