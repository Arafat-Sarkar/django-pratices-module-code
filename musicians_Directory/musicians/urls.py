from django.urls import path
from .import views
urlpatterns = [
    path('add/', views.addMusic, name= 'addMusic' ),
    path('edit/<int:id>',views.edit_music, name='edit_music'),
    #  path('delete/<int:id>',views.delet_music, name='delet_music')
   
]
