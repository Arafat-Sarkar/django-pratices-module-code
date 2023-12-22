from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.home, name= 'homepage'),
    path('register/', views.register, name= 'register'),
    path('login/', views.userlogin.as_view(), name= 'login'),
    path('logout/', views.userlogout.as_view(), name= 'logout'),
    path('profile/', views.profile, name= 'profile'),
   
]
