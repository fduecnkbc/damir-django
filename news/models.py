from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    date = models.DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.date = timezone.now()
        self.save()
	
    def __str__(self):
    	return self.title
