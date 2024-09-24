# Generated by Django 5.1.1 on 2024-09-24 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название клуба')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='club_images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hall_images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
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
            name='ClubAdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='club_images/', verbose_name='Изображение')),
                ('video_link', models.URLField(blank=True, max_length=500, null=True, verbose_name='Ссылка на видео')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_info', to='sport.club', verbose_name='Клуб')),
            ],
            options={
                'verbose_name': 'Дополнительная информация о клубе',
                'verbose_name_plural': 'Дополнительная информация о клубах',
            },
        ),
        migrations.CreateModel(
            name='ClubImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='club_images/', verbose_name='Изображение')),
                ('additional_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sport.clubadditionalinfo', verbose_name='Дополнительная информация')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sport.club', verbose_name='Клуб')),
            ],
            options={
                'verbose_name': 'Изображение клуба',
                'verbose_name_plural': 'Изображения клубов',
            },
        ),
        migrations.CreateModel(
            name='HallArena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('dimensions', models.CharField(max_length=255, verbose_name='Размеры зала')),
                ('capacity', models.CharField(max_length=10, verbose_name='Количество мест')),
                ('type', models.CharField(max_length=100, verbose_name='Тип')),
                ('covering', models.CharField(max_length=100, verbose_name='Покрытие')),
                ('inventory', models.TextField(verbose_name='Инвентарь')),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оплата за час')),
                ('dressing_room', models.BooleanField(default=False, verbose_name='Раздевалка')),
                ('lighting', models.BooleanField(default=False, verbose_name='Освещение')),
                ('shower', models.BooleanField(default=False, verbose_name='Душевая')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_arena', to='sport.hall', verbose_name='зал')),
            ],
            options={
                'verbose_name': 'Арена зала',
                'verbose_name_plural': 'Арены залов',
            },
        ),
        migrations.CreateModel(
            name='HallInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hall_images/', verbose_name='Изображение')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_info', to='sport.hall', verbose_name='зал')),
            ],
            options={
                'verbose_name': 'Информация о зале',
                'verbose_name_plural': 'Информация о залах',
            },
        ),
        migrations.CreateModel(
            name='HallImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hall_images/', verbose_name='Изображение')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sport.hall', verbose_name='Зал')),
                ('hall_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sport.hallinfo', verbose_name='Информация о зале')),
            ],
            options={
                'verbose_name': 'Изображение зала',
                'verbose_name_plural': 'Изображения залов',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('rating', models.PositiveIntegerField(verbose_name='Оценка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='sport.sport', verbose_name='Вид спорта')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='hall',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.sport'),
        ),
        migrations.AddField(
            model_name='club',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clubs', to='sport.sport'),
        ),
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('07:00', '07:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00')], max_length=5, verbose_name='Время')),
                ('day', models.CharField(choices=[('Mon', 'Пн'), ('Tue', 'Вт'), ('Wed', 'Ср'), ('Thu', 'Чт'), ('Fri', 'Пт'), ('Sat', 'Сб')], max_length=3, verbose_name='День')),
                ('age_group', models.CharField(max_length=255, verbose_name='Возрастная группа')),
                ('coach', models.CharField(max_length=255, verbose_name='Тренер')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.sport', verbose_name='Вид спорта')),
            ],
            options={
                'verbose_name': 'Расписание тренировки',
                'verbose_name_plural': 'Расписания тренировок',
            },
        ),
    ]
