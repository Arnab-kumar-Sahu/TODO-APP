from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    data=Todo.objects.filter(user=request.user)
    return render(request,'home.html',{'data':data})
@login_required(login_url='login')
def add(request):

    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        user=request.user
        Todo.objects.create(title=title,desc=desc,user=user)
    return render(request,'add.html')
@login_required(login_url='login')
def delete_(request,pk):
    a=Todo.objects.get(id=pk)
    Trashmodel.objects.create(title=a.title,desc=a.desc,user=request.user)
    a.delete()
    return redirect('home')
@login_required(login_url='login')
def completed(request,pk):
    a=Todo.objects.get(id=pk)
    Completemodel.objects.create(title=a.title,desc=a.desc,user=request.user)
    a.delete()
    return redirect('home')
@login_required(login_url='login')
def deleteall(request):
    a=Todo.objects.all()
    for i in a:
        Trashmodel.objects.create(
            title=i.title,desc=i.desc,user=request.user   
        )
        i.delete()
    return redirect('home')
@login_required(login_url='login')
def update(request,pk):
    data=Todo.objects.get(id=pk)
    if request.method=='POST':
        a=request.POST['title']
        b=request.POST['desc']
        data.title=a
        data.desc=b
        data.save()
        return redirect('home')

    return render(request,'update.html',{'data':data})




@login_required(login_url='login')
def complete(request):
    data=Completemodel.objects.filter(user=request.user)
    return render(request,'complete.html',{'data':data})
@login_required(login_url='login')
def deletecomplete(request,pk):
    a=Completemodel.objects.get(id=pk)
    Trashmodel.objects.create(title=a.title,desc=a.desc,user=request.user)
    a.delete()
    return redirect('complete')
@login_required(login_url='login')
def deleteallcomplete(request):
    a=Completemodel.objects.all()
    for i in a:
        Trashmodel.objects.create(title=i.title,desc=i.desc,user=request.user)
        i.delete()
    return redirect('complete')
@login_required(login_url='login')
def resotrecomplete(request,pk):
    a=Completemodel.objects.get(id=pk)
    Todo.objects.create(title=a.title,desc=a.desc,user=request.user)
    a.delete()
    return redirect('home')





def trash(request):
    data=Trashmodel.objects.filter(user=request.user)
    return render(request,'trash.html',{'data':data})

def deletetrash(request,pk):
    a=Trashmodel.objects.get(id=pk)
    a.delete()
    return redirect('trash')

def deletealltrash(request):
    a=Trashmodel.objects.all()
    a.delete()
    return redirect('trash')

def restoretrash(request,pk):
    a=Trashmodel.objects.get(id=pk)
    Todo.objects.create(title=a.title,desc=a.desc,user=request.user)
    a.delete()
    return redirect('trash')


def about(request):
    return render(request,'about.html')