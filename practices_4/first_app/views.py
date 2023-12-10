from django.shortcuts import render
from .import forms
from .import models
from first_app.forms import listForm

# Create your views here.

def home(request):
    return render (request, 'index.html')

def DForm(request):
    form = forms.djagoFrom()
    return render (request,'django_form.html',{'form':form})

def MForm(request):
    ls = listForm()
    return render(request,'model_form.html', {'ls': ls})