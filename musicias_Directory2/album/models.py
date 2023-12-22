from django.db import models
from musician.models import musicanModel

# Create your models here.
class albumModel(models.Model):
    Rating = {
       (1, "1"),
       (2, "2"),
       (3 ,"3") ,
       (4, "4") ,
       (5, "5")  
    }
   
    Album_Name = models.CharField(max_length= 100)
    music = models.ForeignKey(musicanModel, on_delete= models.CASCADE)
    Album_release_date = models.DateField()
    Rating_between= models.PositiveIntegerField( choices= Rating ,default=5 )
    
    
    def __str__(self):
        return self.Album_Name
     

     