from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def landingView(request):
    return render(request,"landing.html")

def loginview(request):
    if request.method=="GET":
     return render(request,"login.html")
    elif request.method=="POST":
       print(request.POST)
       Username=request.POST.get('uname')
       password=request.POST.get('pswd')
       return redirect('uhome')
    


def registerview(request):
   if request.method=="GET":      
    return render(request,"register.html")
   elif request.method=="POST":
      print(request.POST)
      Firstname=request.POST.get('fname')
      Lastname=request.POST.get('lname')
      Email=request.POST.get('email')
      Username=request.POST.get('uname')
      Password=request.POST.get('pswd')
      return HttpResponse(f"Firstname:{Firstname} ,Lastname:{Lastname} ,Email id:{Email} ,Username:{Username} ,Password:{Password}")

