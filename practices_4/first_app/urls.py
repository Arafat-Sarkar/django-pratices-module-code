from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name= 'homePage'),
    path('Djnao_form/', views.DForm , name= 'D_form'),
    path('model_form/',views.MForm, name= 'M_form')
]
