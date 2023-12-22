from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .import models
from .import forms
from django.urls import reverse_lazy
# Create your views here.
# def Addusic(request):
#     return render (request, 'music.html')

class Addmusic(CreateView):
    model =models.musicanModel
    form_class = forms.musicianForm
    template_name = 'music.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        form.instance = self.request.user
        return super().form_valid(form)
    
class editMusic(UpdateView):
    model = models.musicanModel
    form_class = forms.musicianForm
    template_name = 'music.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
