# Generated by Django 4.2.11 on 2024-08-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('flooring', models.CharField(max_length=255)),
                ('court_count', models.IntegerField()),
                ('equipment', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('changing_room', models.BooleanField(default=True)),
                ('lighting', models.BooleanField(default=True)),
                ('shower', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('advantages', models.TextField()),
                ('client_reviews', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('experience', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experience', models.IntegerField(help_text='Количество лет опыта')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('arena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bilimkana.arena')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('day', models.CharField(choices=[('Mon', 'Понедельник'), ('Tue', 'Вторник'), ('Wed', 'Среда'), ('Thu', 'Четверг'), ('Fri', 'Пятница'), ('Sat', 'Суббота'), ('Sun', 'Воскресенье')], max_length=3)),
                ('time', models.TimeField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilimkana.trainer')),
            ],
        ),
    ]