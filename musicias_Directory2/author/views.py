from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from album.models import albumModel

# Create your views here.
def home(request):
    return render(request, 'index.html')

def profile(request):
        data = albumModel.objects.all()
        return render(request, 'profile.html',{'data':data})
  

def register(request):
    if request.method == 'POST':
        resiter_form = forms.registerform(request.POST)
        if resiter_form.is_valid():
            resiter_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
        
    else :
        resiter_form = forms.registerform(request.POST)
    return render (request, 'register.html', {'form': resiter_form, 'type':'Register'})

class userlogin(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self,form):
        messages.success(self.request, 'Loggin successfully')
        return super().form_valid(form)
    
    def  form_invalid(self, form):
        messages.success(self.request, 'Loggin incorent')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
       
class userlogout(LogoutView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('register')
    # def form_valid(self,form):
    #     messages.success(self.request, 'Logout successfully')
    #     return super().form_valid(form)


