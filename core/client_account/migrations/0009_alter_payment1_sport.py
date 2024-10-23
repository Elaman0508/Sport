# Generated by Django 5.1.1 on 2024-10-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_account', '0008_alter_payment1_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment1',
            name='sport',
            field=models.CharField(choices=[('баскетбол', 'Баскетбол'), ('футбол', 'Футбол'), ('волейбол', 'Волейбол'), ('теннис', 'Тенис'), ('бокс', 'Бокс'), ('велоспорт', 'Велоспорт'), ('таэквондо', 'Таэквондо'), ('плавание', 'Плавание'), ('йога', 'Йога')], max_length=100, verbose_name='Виды спорта'),
        ),
    ]
