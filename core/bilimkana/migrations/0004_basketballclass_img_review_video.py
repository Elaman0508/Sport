# Generated by Django 5.1.1 on 2024-09-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilimkana', '0003_alter_registration_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketballclass',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='class_images/'),
        ),
        migrations.AddField(
            model_name='review',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]