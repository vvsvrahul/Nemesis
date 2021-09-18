from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from blog1.forms import *
from blog1.models import *
from django.contrib.auth.models import User
# Create your views here.

def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('blog1:blogs'))
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('pass')
            user = authenticate(username= username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('blog1:blogs'))
                else:
                    return HttpResponse("Account not active")
            else:
                print("someone tried to login and failed ")
                print(f"Username :{username} and password :{password}")
                return HttpResponse("Invalid login credentials")

        else:
            return render(request,'blog1/login.html',context={})

# @login_required
def next1(request):
    return render(request,'blog1/after.html',context={})

@login_required
def userlogout(request):
    logout(request)
    return render(request,'blog1/login.html')
#
def registration(request):
    registered = False
    if request.method == "POST":


        user_form = authenticateform(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            email = user_form.cleaned_data.get('email')
            address = request.POST.get("address")
            print(username,password,address)
            user_obj = User(username=username,password= password,email=email)
            user_obj.set_password(user_obj.password)
            user_obj.save()
            address = UserAddress(user=user_obj,address=address)
            address.save()
            registered = True
    
            return HttpResponseRedirect(reverse('blog1:congo'))
        else:
            print(user_form.errors)
            return HttpResponse("Some error occured")
    else:

        context={"registered":registered}
        return render(request,'blog1/signup1.html',context)


## this works too
# def registration(request):
#     registered = False
#     if request.method == "POST":
#
#
#         user_form = authenticateform(request.POST)
#
#         if user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             registered = True
#         else:
#             print(user_form.errors)
#     else:
#         form =  authenticateform()
#         context={'registered':registered,'form':form}
#         return render(request,'blog1/signup1.html',context)
def congo(request):
    return render(request,'blog1/congrats.html',)


@login_required
def postmaker(request):
    return render(request,'blog1/blogs.html')


def update(request,pk):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        newusername = request.POST.get("username")
        newemail = request.POST.get("email")
        user.username = newusername
        user.email = newemail
        user.save()    
        newaddress= request.POST.get("address")
        n = UserAddress.objects.get( id=pk)
        n.address = newaddress
        n.save()
        return HttpResponseRedirect(reverse('blog1:login'))
    else:   
        return render(request,'blog1/update.html')

def Delete(request,pk):
   
    user = User.objects.get(id=pk)
    logout(request)
    user.delete()
    return HttpResponseRedirect(reverse('blog1:login'))




