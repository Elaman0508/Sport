# Generated by Django 5.1.1 on 2024-10-23 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment1',
            old_name='age_group',
            new_name='age',
        ),
    ]