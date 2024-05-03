# Generated by Django 3.2 on 2024-05-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='course_pdfs/%Y/%m/%d/'),
        ),
    ]