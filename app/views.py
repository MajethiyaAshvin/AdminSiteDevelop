from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from app.models import User
def index(request):
  return render(request,"index.html")
def register(request):
  return render(request,"register.html")
def doLogin(request):
 n=request.POST.get("username")
 p=request.POST.get("password")
 if n=="ashvin" and p=="123456":
  return render(request,"home.html")
 else:
  return HttpResponse("invalid Credentials ***")

def doRegister(request):
 fname=request.POST.get("fname")
 mname=request.POST.get("mname")
 lname = request.POST.get("lname")
 mobile = request.POST.get("mobile")
 password = request.POST.get("password")
 confirmpass = request.POST.get("cpassword")
 register=User(firstname=fname,midlename=mname,lastname=lname,mobile=mobile,password=password,confoirmpassword=confirmpass)
 register.save();
 return  HttpResponse("Register successfully.!")