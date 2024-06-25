from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import Permission

class User(AbstractUser):
    MASTER_ROLE = 'Master'
    TEACHER_ROLE = 'Teacher'
    STUDENT_ROLE = 'Student'
    
    ROLE_CHOICES = [
        (MASTER_ROLE, 'Master'),
        (TEACHER_ROLE, 'Teacher'),
        (STUDENT_ROLE, 'Student'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT_ROLE)
    user_groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="teachers/%Y/%m/%d/")
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    user_groups = models.ManyToManyField(Group, related_name='teacher_user_groups')

    def __str__(self):
        return self.user.username
