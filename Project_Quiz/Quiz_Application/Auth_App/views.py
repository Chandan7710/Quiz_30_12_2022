from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Home_App.models import User

# Create your views here.

def profile(request):
    return render(request, 'Auth_App/profile.html')

def authregistration(request):
    if request.method == 'POST':
        registration_username = request.POST['name']
        registration_email = request.POST['email']
        registration_password = request.POST['password']
        registration_confirm_password = request.POST['confirm_password']
        if registration_password == registration_confirm_password:
            
            if User.objects.filter(username=registration_username).exists():
                messages.error(request, 'Username Already Exists')
            elif User.objects.filter(email=registration_email).exists():
                messages.error(request, 'Email Already Exists')
            else:
                registration_user = User.objects.create_user(username=registration_username, password=registration_password, email=registration_email)
                registration_user.save()
                messages.success(request, 'You have Successfully Registered')
                return redirect('login')
        else:
            messages.error(request, 'Password and Conform Password Not Matched')
    
    return render(request, 'Auth_App/registration.html')


def authlogin(request):
    if request.method == 'POST':
        login_email = request.POST['email']
        login_password = request.POST['password']
        auth_user = authenticate(request, email=login_email, password=login_password)
        
        if auth_user is not None:
            login(request, auth_user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password Invalid !')
        
    return render(request, 'Auth_App/login.html')

def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')

