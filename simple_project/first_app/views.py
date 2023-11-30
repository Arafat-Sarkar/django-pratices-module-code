from django.shortcuts import render
import datetime

# Create your views here.

def home (request):
    d= {'author ' : 'Rahim' , 'age' : 30 , 'lst':['pitron','is','best'] , 'birthdate' : datetime.datetime.now() , 'val': 5, 'capital': "arafat", 'cut':'ptrion is fun','food': ['Apple', 'Mango', 'Orange'], 'low':'I Am Master Yoda','titel' : "It's a new day" ,}
    return  render(request , "home.html", d)