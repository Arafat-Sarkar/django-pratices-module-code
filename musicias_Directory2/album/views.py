from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .import models
from .import forms
from django.urls import reverse_lazy

# Create your views here.
class create_album(CreateView):
    model = models.albumModel
    form_class = forms.albumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditAlbum(UpdateView):
    model = models.albumModel
    form_class = forms.albumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
class DeletAlbum(DeleteView):
    model = models.albumModel
    template_name = 'deletd.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    