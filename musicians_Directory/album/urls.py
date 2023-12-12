from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.AddAlbum, name = "addAlbum"),
     path('edit/<int:id>',views.edit_album, name='edit_album'),
     path('delete/<int:id>',views.delet_album, name='delet_album')
]
