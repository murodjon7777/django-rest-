from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    file=models.FileField()
    
    
    def __str__(self) -> str:
        return self.title
