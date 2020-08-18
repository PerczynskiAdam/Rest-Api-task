from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=100, blank = True, null = True)
   authors = models.CharField(max_length=100, blank = True, null = True)
   published_date = models.CharField(max_length=100, blank = True, null = True)
   categories = models.CharField(max_length=100, blank = True, null = True)
   average_rating = models.FloatField(blank = True, null = True)
   ratings_count = models.IntegerField(blank = True, null = True)
   thumbnail = models.URLField(max_length=200, blank = True, null = True)
   
   def __str__(self):
      return self.title