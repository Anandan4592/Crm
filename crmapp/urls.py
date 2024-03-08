from django.urls import path
from. import views

urlpatterns = [
    path('',views.crmhome,name='crmhome'),
    path('crmnavv',views.crmnavv,name='crmnavv'),
    path('crmsignin',views.crmsignin,name='crmsignin'),
    path('crmregister',views.crmregister,name='crmregister'),
    path('register',views.register,name='register'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('crmloginpage',views.crmloginpage,name='crmloginpage'),
     
]