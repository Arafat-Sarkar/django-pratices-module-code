from django.urls import path
from .import views

urlpatterns = [
    path('music/',views.Addmusic.as_view(), name='music' ),
    path('editmusic/<int:id>',views.editMusic.as_view(),name= 'editmusic')
]
