# Generated by Django 5.1.1 on 2024-09-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gyminfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportclass',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='class_images/'),
        ),
    ]