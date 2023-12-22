from django.shortcuts import render, redirect
from first_app.forms import registerForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash

# Create your views here.

def home (request):
    return render (request, 'home.html')

def register(request):
    # if not request.user.is_authenticated:
        if request.method =="POST":
            form = registerForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Succesfully')
                form.save()
                print(form.cleaned_data)
        
        else:
            form = registerForm()
        return render(request, 'register.html',{'form':form})
        
    # else:
    #     return redirect ('home')
    
    
def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass= form.cleaned_data['password']
            user = authenticate(username = name , password = userpass)
            if user is not None:
                    messages.success(request, 'Logout Successfully') 
                    login(request, user)
                    return redirect('profile')
            else:
                messages.success(request, 'Logout Successfully') 
                return redirect('register')
                
    
    else:
        form = AuthenticationForm()
    return render (request, 'login.html',{'form': form})
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user':request.user})
    else:
        return redirect('login')
        
        
 

def userlogout(request):
    logout(request)
    return redirect('register')

def changePass(request):
    if request.method =="POST":
        form = PasswordChangeForm(user= request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'changeForm.html',{'form': form})

def changePass2(request):
    if request.method =="POST":
        form = SetPasswordForm(user= request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'changeForm.html',{'form': form})
            
            