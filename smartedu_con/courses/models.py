from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/default_course_image.png")
    date = models.DateTimeField(auto_now=True)
    avaliable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name