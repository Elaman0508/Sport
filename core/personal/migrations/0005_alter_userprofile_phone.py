# Generated by Django 5.1.1 on 2024-09-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]