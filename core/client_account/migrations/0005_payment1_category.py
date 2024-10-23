# Generated by Django 5.1.1 on 2024-10-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_account', '0004_remove_payment1_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment1',
            name='category',
            field=models.CharField(choices=[('Взрослые', 'Взрослые'), ('Подростки', 'Подростки'), ('Дети', 'Дети')], default=1, max_length=20, verbose_name='Возрастная группа'),
            preserve_default=False,
        ),
    ]
