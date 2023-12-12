from django.db import models
from musicians.models import Musican

# Create your models here.
class Album(models.Model):
    Rating = {
       (1, "1"),
       (2, "2"),
       (3 ,"3") ,
       (4, "4") ,
       (5, "5")  
    }
    Album_Name = models.CharField(max_length= 100)
    music = models.ForeignKey(Musican,on_delete=models.CASCADE) 
    Album_relese_Date = models.DateTimeField(auto_now=True)
 
    Rating_between= models.PositiveIntegerField( choices= Rating ,default=5 )
    
    def __str__(self):
        return self.Album_Name