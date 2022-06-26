from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from . models import *

# Create your views here.

def indexX(request):
    return render(request,'indexC.html') 


def login(request):
    return render(request,'LoginForm.html') 

def adlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if freg.objects.filter(email=email,password=password).exists():
        data=freg.objects.filter(email=email,password=password).values('username','id').first()
        request.session['username']=data['username']
        request.session['email']=email
        request.session['password']= password
        request.session['id']=data['id']
        return redirect('REG') 
    else:
        return render(request,'LoginForm.html',{'msg':"Sorry... Invalid username or password"})  

def adlogout(request):
    del request.session['email']
    del request.session['username']
    del request.session['password']
    del request.session['id']
    return redirect('REG') 

def RegForm(request):
    return render(request,'RegisterForm.html')  

def regdisplay(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        data = freg(username=username,password=password,repassword=repassword,email=email)
        data.save()
    return redirect('login')   

def REG(request):
    return render(request,'regForm.html')

def Cdisplay(request):
    if request.method=='POST':
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        adrs = request.POST.get('adrs')
        Relationship = request.POST.get('Relationship')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        number = request.POST.get('number')
        img = request.FILES['img']
        data = Creg(Fname=Fname,Lname=Lname,adrs=adrs,location=location,Relationship=Relationship,gender=gender,number=number,img=img)
        data.save()
        return redirect('indexX')    


def Cedit(request,eid):
    data = Creg.objects.filter(id=eid)
    return render(request,'editreg.html',{'data':data})    

def Cupdate(request,uid):   
    if request.method=='POST':
        Fname = request.POST.get('fname')
        Lname = request.POST.get('lname')
        adrs = request.POST.get('adrs')
        Relationship = request.POST.get('Relationship')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        number = request.POST.get('number')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=Creg.objects.get(id=uid).img
        data = Creg(Fname=Fname,Lname=Lname,adrs=adrs,location=location,Relationship=Relationship,gender=gender,number=number,img=file)
    return redirect('indexX')

def Cdelete(request,did):
       data = Creg.objects.filter(id=did)
       data.delete()
       return redirect('indexX')  

def EditR(request):
    userid=request.session.get('id')
    data1=Creg.objects.all()
    data=Creg.objects.filter(userid=userid)
    return render(request,'viewprofile.html',{'data1':data1,'data':data})