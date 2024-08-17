# Generated by Django 5.0.6 on 2024-08-17 19:06

import django.db.models.deletion
from django.db import migrations, models


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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('arena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bilimkana.arena')),
            ],
        ),
    ]
