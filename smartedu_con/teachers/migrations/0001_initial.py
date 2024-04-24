# Generated by Django 5.0.4 on 2024-04-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='courses/%Y/%m/%d/')),
                ('linkedin', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
            ],
        ),
    ]
