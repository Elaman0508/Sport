# Generated by Django 5.1 on 2024-08-30 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('sports', models.CharField(choices=[('basketball', 'Баскетбол'), ('football', 'Футбол'), ('volleyball', 'Волейбол'), ('tennis', 'Тенис'), ('boxing', 'Бокс'), ('cycling', 'Велоспорт'), ('taekwondo', 'Таэквондо'), ('swimming', 'Плавание'), ('yoga', 'Йога')], max_length=20, verbose_name='Виды спорта')),
                ('header1', models.CharField(blank=True, max_length=255, verbose_name='Заголовок 1')),
                ('header2', models.CharField(blank=True, max_length=255, verbose_name='Заголовок 2')),
                ('header3', models.CharField(blank=True, max_length=255, verbose_name='Заголовок 3')),
                ('header4', models.CharField(blank=True, max_length=255, verbose_name='Заголовок 4')),
                ('description1', models.TextField(blank=True, verbose_name='Описание 1')),
                ('description2', models.TextField(blank=True, verbose_name='Описание 2')),
                ('description3', models.TextField(blank=True, verbose_name='Описание 3')),
                ('description4', models.TextField(blank=True, verbose_name='Описание 4')),
            ],
            options={
                'verbose_name': 'Кружок',
                'verbose_name_plural': 'Кружки',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('sports', models.CharField(choices=[('basketball', 'Баскетбол'), ('football', 'Футбол'), ('volleyball', 'Волейбол'), ('tennis', 'Тенис'), ('boxing', 'Бокс'), ('cycling', 'Велоспорт'), ('taekwondo', 'Таэквондо'), ('swimming', 'Плавание'), ('yoga', 'Йога')], max_length=20, verbose_name='Виды спорта')),
                ('size', models.CharField(max_length=50, verbose_name='Размеры зала')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('hall_type', models.CharField(max_length=100, verbose_name='Тип')),
                ('coverage', models.CharField(max_length=100, verbose_name='Покрытие')),
                ('inventory', models.TextField(verbose_name='Инвентарь')),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оплата за час')),
                ('dressing_room', models.BooleanField(default=False, verbose_name='Раздевалка')),
                ('lighting', models.BooleanField(default=False, verbose_name='Освещение')),
                ('shower', models.BooleanField(default=False, verbose_name='Душевая')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='CircleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='circle_images/', verbose_name='Фото')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circle_images', to='about_admin.circle', verbose_name='Кружок')),
            ],
            options={
                'verbose_name': 'Фото кружка',
                'verbose_name_plural': 'Фото кружков',
            },
        ),
        migrations.AddField(
            model_name='circle',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='circles', to='about_admin.circleimage', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='HallImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hall_images/', verbose_name='Изображение')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='about_admin.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Изображение зала',
                'verbose_name_plural': 'Изображения залов',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=9, verbose_name='День недели')),
                ('start_time', models.TimeField(verbose_name='Время начала')),
                ('end_time', models.TimeField(verbose_name='Время окончания')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='about_admin.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
                'ordering': ['day_of_week', 'start_time'],
            },
        ),
    ]
