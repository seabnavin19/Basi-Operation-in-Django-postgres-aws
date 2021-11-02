from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, authenthicated_user
from django.contrib.auth.models import Group


# Create your views here.
from django.http import HttpResponse
from .models import *
from .form import *

@login_required(login_url="loginUser")
@allowed_users(allowed_roles=["admin"])
def home(request):
    post=Post.objects.all()
    return render(request,"sell_house/home.html",{"posts":post})

@login_required(login_url="loginUser")
def sell(request,pk):
    sell= Post.objects.get(id=pk)
    return render(request,"sell_house/selling.html",{"sells":sell})

@login_required(login_url="loginUser")
def CreateSell(request):
    form= SellForm()
    if request.method=='POST':
        form =SellForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
    context={"form":form}
    return render(request,"sell_house/create.html",context)

@login_required(login_url="loginUser")

def UpdatePost(request,pk):
    sell=Post.objects.get(id=pk)
    form =SellForm(instance=sell)
    if request.method=="POST":
        form=SellForm(request.POST,instance=sell)
        if form.is_valid:
            form.save()
            return redirect("/")
    context = {"form":form}
    return render(request,"sell_house/create.html",context)

@login_required(login_url="loginUser")
def DeletePost(request,pk):
    sell=Post.objects.get(id=pk)
    if request.method=="POST":
        sell.delete()
        return redirect("/")
        

    context={"item":sell}
    return render(request,"sell_house/delete.html",context)

def CreateUser(request):
    userform=CreateUserForm()
    if request.method=="POST":
        userform=CreateUserForm(request.POST)
        if userform.is_valid:
            user=userform.save()
            group=Group.objects.get(name="customer")
            user.groups.add(group)

            return redirect("home")

    context={"userForm":userform}
    return render(request,"sell_house/register.html",context)

@authenthicated_user
def LoginUser(request):
    # print(username)
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")

        return render(request,"sell_house/login.html")

def LogoutUser(request):
    logout(request)
    return redirect("loginUser")

# @authenthicated_user
# @allowed_users(allowed_roles=["customer"])
def Userpage(request):
    dat=request.user.User.objects.all()
    context={"user_data":dat}
    return render(request,"sell_house/user.html",context)

