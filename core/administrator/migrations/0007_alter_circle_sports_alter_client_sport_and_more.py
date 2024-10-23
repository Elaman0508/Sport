# Generated by Django 5.1.1 on 2024-10-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_schedul_is_active_schedul_сircle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='sports',
            field=models.CharField(choices=[('Баскетбол', 'Баскетбол'), ('Футбол', 'Футбол'), ('Волейбол', 'Волейбол'), ('Тенис', 'Тенис'), ('Бокс', 'Бокс'), ('Велоспорт', 'Велоспорт'), ('Таэквондо', 'Таэквондо'), ('Плавание', 'Плавание'), ('Йога', 'Йога')], max_length=20, verbose_name='Виды спорта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='sport',
            field=models.CharField(choices=[('Баскетбол', 'Баскетбол'), ('Футбол', 'Футбол'), ('Волейбол', 'Волейбол'), ('Тенис', 'Тенис'), ('Бокс', 'Бокс'), ('Велоспорт', 'Велоспорт'), ('Таэквондо', 'Таэквондо'), ('Плавание', 'Плавание'), ('Йога', 'Йога')], max_length=20, verbose_name='Спорт'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='sports',
            field=models.CharField(choices=[('Баскетбол', 'Баскетбол'), ('Футбол', 'Футбол'), ('Волейбол', 'Волейбол'), ('Тенис', 'Тенис'), ('Бокс', 'Бокс'), ('Велоспорт', 'Велоспорт'), ('Таэквондо', 'Таэквондо'), ('Плавание', 'Плавание'), ('Йога', 'Йога')], max_length=20, verbose_name='Виды спорта'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='sport',
            field=models.CharField(choices=[('Баскетбол', 'Баскетбол'), ('Футбол', 'Футбол'), ('Волейбол', 'Волейбол'), ('Тенис', 'Тенис'), ('Бокс', 'Бокс'), ('Велоспорт', 'Велоспорт'), ('Таэквондо', 'Таэквондо'), ('Плавание', 'Плавание'), ('Йога', 'Йога')], max_length=20, verbose_name='Спорт'),
        ),
    ]
