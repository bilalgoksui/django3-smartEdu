from django.contrib import admin
from .models import Student


@admin.register(Student)
class AccountAdmin(admin.ModelAdmin):
    list_display= ('user'),
