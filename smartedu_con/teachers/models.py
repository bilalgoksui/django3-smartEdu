from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/")
    linkedin = models.URLField(max_length=200,blank=True)
    facebook = models.URLField(max_length=200,blank=True)
    
    def __str__(self):
        return self.name