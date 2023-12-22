from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('register/',views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name= 'profile'),
    path('logout/', views.userlogout, name= 'logout'),
    path('passchange/', views.changePass, name='passchange'),
    path('passchange2/', views.changePass2, name='passchange2')
]
