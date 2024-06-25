from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MinValueValidator

class User(AbstractUser):
    MASTER_ROLE = 'Master'
    TEACHER_ROLE = 'Teacher'
    STUDENT_ROLE = 'Student'
    
    ROLE_CHOICES = [
        (MASTER_ROLE, 'Master'),
        (TEACHER_ROLE, 'Teacher'),
        (STUDENT_ROLE, 'Student'),
    ]
    
    groups = models.ManyToManyField(Group)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT_ROLE)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="students/%Y/%m/%d/")
    user_groups = models.ManyToManyField(Group, related_name='student_user_groups')

    def __str__(self):
        return self.user.username
