from django.urls import path
from .import views
urlpatterns = [
    
    path('album/',views.create_album.as_view(),name='album'),
    path('editAlbum/<int:id>', views.EditAlbum.as_view(), name= 'edit'),
    path('delet/<int:id>', views.DeletAlbum.as_view(), name= 'delet')
    
]
