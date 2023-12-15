from django.db import models
from musician.models import Musician
CHOICES = (
      ('1', 1),
      ('2',2 ),
      ('3', 3),
      ('4', 4),
      ('5', 5),
      
  )
# Create your models here.
class AlbumModel(models.Model):
    Album_name = models.CharField(max_length=40)
    Album_release_date = models.DateField(auto_now_add=True)
    Rating_between = models.CharField(max_length=1,choices=CHOICES)
    musicians = models.ForeignKey(Musician,on_delete=models.CASCADE , related_name='albums')
    
    def __str__(self):
        return self.Album_name