from django.shortcuts import render,redirect
from .import models
from .import forms

# Create your views here.

def addMusic(request):
    if request.method == 'POST':
        add_music =  forms.addForm(request.POST)
        if add_music.is_valid():
            add_music.save()
            return redirect('addAlbum')
        
    else:
     add_music =  forms.addForm()  
     return render(request, 'add_music.html',{'form':add_music})
 
def edit_music(request,id):
    music= models.Musican.objects.get(pk=id)
    add_music =  forms.addForm(instance=music)
    if request.method == 'POST':
        add_music =  forms.addForm(request.POST,instance=music)
        if add_music.is_valid():
            add_music.save()
            return redirect('homepage')
        
    else:
     add_music =  forms.addForm()  
     return render(request, 'add_music.html',{'form':add_music})

 
     
# def delet_music(request,id):
#     music= models.Musican.objects.get(pk=id)
#     music.delete()
#     return redirect('homepage')