from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=="POST":
        a=request.POST['firstname']
        b=request.POST['lastname']
        c=request.POST['username']
        d=request.POST['password']
        e=request.POST['email']
        if not (re.search('[A-Z]',d) and re.search('[@#$&_]',d) and re.search('[0-9]',d) and re.search('[a-z]',d) ):
            return render(request,'register.html',{'invalid':True})
        try:
            A=User.objects.get(username=c)
            return render(request,'register.html',{"exists":True})
        except:
            A=User.objects.create(first_name=a,last_name=b,username=c,email=e)
            A.set_password(d)
            A.save()
            return redirect('login')
    return render(request,'register.html')
def authlogin(request):
    if request.method=="POST":
        a=request.POST['username']
        b=request.POST['password']
        obj=authenticate(username=a,password=b)
        if obj:
            login(request,obj)
            return redirect('home')
        else:
            return render(request,'login.html',{"error":True})
    return render(request,'login.html')
@login_required(login_url='login')
def authlogout(request):
    logout(request)
    return redirect('login')