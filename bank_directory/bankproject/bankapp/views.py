from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Form,District,Branch

# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        # return redirect('newpage')
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,"Enter valid Username and password.")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def newpage(request):
    return render(request,"newpage.html")
def detailfill(request):
    district = District.objects.all()
    branch = Branch.objects.all()
    if request.method=='POST':
        name = request.POST.get('name',)
        date = request.POST.get('date',)
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        form=Form(name=name,date=date,age=age,gender=gender,phone=phone,email=email,address=address)
        form.save()
        # if form is not None:
        #     form.save()
        return redirect('lastpage')
        # else:
        #     messages.info(request, "Enter valid Username and password.")
        #     return redirect('detailfill')

    return render(request,"detailfill.html",{'district':district,'branch':branch})

# def detailfill(request):
#     if request.method=='POST':
#         name = request.POST.get('name',)
#         date = request.POST.get('date',)
#         age = request.POST.get('age', )
#         gender = request.POST.get('gender', )
#         phone = request.POST.get('phone', )
#         email = request.POST.get('email', )
#         address = request.POST.get('address', )
#         form=Form(name=name,date=date,age=age,gender=gender,phone=phone,email=email,address=address)
#         form.save()
#         return redirect('lastpage')
#     return render(request,"detailfill.html")
def lastpage(request):
    return render(request,"lastpage.html")
# def formfill(request):
#     district=District.objects.all()
#     branch=Branch.objects.all()
#     return render(request,"detailfill.html",{'district':district,'branch':branch})
