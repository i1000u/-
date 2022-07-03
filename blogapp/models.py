from django.db import models



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200, default = '천우')
    pub_date = models.DateTimeField('data published')
    body = models.TextField(blank = False)
    writer = models.CharField(max_length = 20)
  
    HAPPY = 'HAPPY'
    SAD = 'SAD'
    ANGRY = 'ANGRY'
    JEALOUS = 'JEALOUS'
    CHOICES = [(HAPPY,'happy'),(SAD,'sad'),(ANGRY,'angry'),(JEALOUS,'jealous')]
    today_feeling = models.CharField(max_length = 10, choices = CHOICES, null = True) 
   

    def __str__(self):
        return self.title
