from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.
def AddAlbum(request):
    if request.method == 'POST':
       album_form = forms.albumForm(request.POST) 
       if album_form.is_valid():
           album_form.save()
           return redirect('homepage')
       
    else:
       album_form = forms.albumForm()   
       return render(request, 'add_album.html', {'form':album_form})
   
    
def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.albumForm(instance= album) 
    if request.method == 'POST':
       album_form = forms.albumForm(request.POST, instance=album) 
       if album_form.is_valid():
           album_form.save()
           return redirect('homepage')
       
    else:
       album_form = forms.albumForm()   
       return render(request, 'add_album.html', {'form':album_form})


def delet_album(request,id):
     album = models.Album.objects.get(pk=id)
     album.delete()
     return redirect('homepage')
       