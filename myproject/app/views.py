from django.shortcuts import render,redirect
from app.models import *
# Create your views here.
def home(request):
    data=Todo.objects.all()
    return render(request,'home.html',{'data':data})
def add(request):

    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        Todo.objects.create(title=title,desc=desc)
    return render(request,'add.html')

def delete_(request,pk):
    a=Todo.objects.get(id=pk)
    Trashmodel.objects.create(title=a.title,desc=a.desc)
    a.delete()
    return redirect('home')

def completed(request,pk):
    a=Todo.objects.get(id=pk)
    Completemodel.objects.create(title=a.title,desc=a.desc)
    a.delete()
    return redirect('home')
    
def deleteall(request):
    a=Todo.objects.all()
    for i in a:
        Trashmodel.objects.create(
            title=i.title,desc=i.desc   
        )
        i.delete()
    return redirect('home')

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





def complete(request):
    data=Completemodel.objects.all()
    return render(request,'complete.html',{'data':data})

def deletecomplete(request,pk):
    a=Completemodel.objects.get(id=pk)
    Trashmodel.objects.create(title=a.title,desc=a.desc)
    a.delete()
    return redirect('complete')

def deleteallcomplete(request):
    a=Completemodel.objects.all()
    for i in a:
        Trashmodel.objects.create(title=i.title,desc=i.desc)
        i.delete()
    return redirect('complete')

def resotrecomplete(request,pk):
    a=Completemodel.objects.get(id=pk)
    Todo.objects.create(title=a.title,desc=a.desc)
    a.delete()
    return redirect('home')





def trash(request):
    data=Trashmodel.objects.all()
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
    Todo.objects.create(title=a.title,desc=a.desc)
    a.delete()
    return redirect('trash')


def about(request):
    return render(request,'about.html')