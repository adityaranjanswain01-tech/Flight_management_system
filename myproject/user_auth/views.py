from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method=='POST':
        try:
            u =User.objects.get(username = request.POST['username'])
            return render(request,'register.html',{"error":"user name already exists"})
        except:
            u = User.objects.create(
                first_name = request.POST['fname'],
                last_name = request.POST['lname'],
                email = request.POST['email'],
                username = request.POST['username'],
            )
            u.set_password(request.POST['password'])
            u.save()
    return render(request,'register.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

def login_(request):
    if request.method=='POST':
        u=authenticate(username = request.POST['username'],password=request.POST['password'])
        if u:
            login(request,u)
            return redirect("home")
        else:
            return render(request,'login.html',{'error':"Ivalid Credentials"})
    return render(request,'login.html')

@login_required(login_url='login')
def logout_(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def reset_pass(request):
    print(request.POST)
    user = request.user 
    if request.method == 'POST':
        if 'old_pass' in request.POST:
            old = request.POST['old_pass']#old pass entered to user
            print(old)
            u = authenticate(username = user.username,password = old)
            print(u)
            if u:
                return render(request,'reset.html',{'new_pass':True})
            else:
                return render(request,'reset.html',{'error':'Old password is incorrect'})
        if 'new_pass' in request.POST:
            new = request.POST['new_pass']
            print(new)
            if user.check_password(new):
                return render(request,'reset.html',{'error':'New password can not be same as old password'})
            user.set_password(new)
            user.save()
            return redirect('login') 
    return render(request,'reset.html')

def forget_pass(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)#meghana
        try:
            u = User.objects.get(username=username)
            print(u)
            request.session['fp_user'] = u.username
            return redirect('new_password')
        except:
            return render(request,'forget.html',{'error':'Invalid Username'})
    return render(request,'forget.html')

def new_password(request):
    username = request.session.get('fp_user')
    print(username)
    if username is None:
        return redirect('forget_pass')
    user = User.objects.get(username=username)
    if request.method == 'POST':
        new_pass = request.POST['new']
        if user.check_password(new_pass):
            return render(request,'new.html',{'error':'New Password should not be same as old password'})
        user.set_password(new_pass)
        user.save()
        del request.session['fp_user']
        return redirect('login')
    return render(request,'newpass.html')