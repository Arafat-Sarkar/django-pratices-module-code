from django.db import models

# Create your models here.
class musicanModel(models.Model):
    First_Name = models.CharField(max_length= 100)
    Last_Name = models.CharField(max_length= 100)
    Email = models.EmailField()
    Instrument_Type = models.CharField(max_length=100)
    PhoneNumber = models.IntegerField()
    
    def __str__(self):
        return f' {self.First_Name}{ self.Last_Name}'
    
    

