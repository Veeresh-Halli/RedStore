from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.


def index(request):
    sdata = request.session.get('uid', default='Guest')
   
    return render(request,'index.html', {'sdata': sdata })

def products(request):

    prods=Products.objects.all()

    return render(request,'products.html', {'prods': prods})    

def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('User successfully created....')

    return render(request,'account.html')
  

def logoutPage(request):
    request.session.flush()
    
    return redirect('account')
    

def loginPage(request):
    if request.method == "POST":
       username = request.POST.get('username')
       password = request.POST.get('password')
       print("Username password saved....")
       user = authenticate(request, username=username, password=password)
       print("Checked...")
       
       if user is not None:
           request.session['uid'] = username
           login(request, user)
           print("After login...")
           return redirect('/') 
        
    return render(request, 'account.html')
    

def cart(request):

    if request.session.has_key('uid'):
       items = cartItems.objects.all()
    else:
       return render(request,'account.html')
    return render(request,'cart.html',{'items': items})   

def productdetail(request,id):

    context = {
        'prod' : get_object_or_404(Products,pk=id)
    }
  
    return render(request,'productdetail.html',context)    


def updateItem(request):
    
       data = json.loads(request.body)
       productId = data['productId']
       action = data['action']

       print("ProductId:", productId)
       print("action:", action)

       product = Products.objects.get(id=productId)
       orderItem , created = cartItems.objects.get_or_create(product=product)
    
    
       if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
       elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1) 
    
    
       orderItem.save()
  


       if orderItem.quantity <= 0:
         orderItem.delete()
        

       return JsonResponse("Item was added", safe=False)