# Generated by Django 5.1.1 on 2024-10-24 05:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('basketball', 'Баскетбол'), ('football', 'Футбол'), ('tennis', 'Теннис'), ('swimming', 'Плавание'), ('volleyball', 'Волейбол'), ('taekwondo', 'Тхэквондо'), ('boxing', 'Бокс'), ('cycling', 'Велоспорт'), ('yoga', 'Йога')], max_length=50, verbose_name='Вид спорта')),
            ],
            options={
                'verbose_name': 'Вид спорта',
                'verbose_name_plural': 'Виды спорта',
            },
        ),
        migrations.CreateModel(
            name='Payment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('баскетбол', 'Баскетбол'), ('футбол', 'Футбол'), ('волейбол', 'Волейбол'), ('теннис', 'Тенис'), ('бокс', 'Бокс'), ('велоспорт', 'Велоспорт'), ('таэквондо', 'Таэквондо'), ('плавание', 'Плавание'), ('йога', 'Йога')], max_length=100, verbose_name='Виды спорта')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата записи')),
                ('opening_time', models.TimeField(verbose_name='Время открытия')),
                ('closing_time', models.TimeField(verbose_name='Время закрытия')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активное расписание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.CreateModel(
            name='Schedul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('понедельник', 'Понедельник'), ('вторник', 'Вторник'), ('среда', 'Среда'), ('четверг', 'Четверг'), ('пятница', 'Пятница'), ('суббота', 'Суббота'), ('воскресенье', 'Воскресенье')], max_length=12, verbose_name='День недели')),
                ('category', models.CharField(choices=[('взрослые', 'Взрослые'), ('подростки', 'Подростки'), ('дети', 'Дети')], max_length=10, verbose_name='Категория')),
                ('start_time', models.TimeField(verbose_name='Начало занятия')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='Окончание занятия')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активное расписание')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Платежи', to='client_account.payment1', verbose_name='')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_account.schedule')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_account.sport'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
