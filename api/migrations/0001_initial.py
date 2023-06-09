# Generated by Django 4.1.7 on 2023-03-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalPath',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('a_lat', models.FloatField()),
                ('a_lon', models.FloatField()),
                ('b_lat', models.FloatField()),
                ('b_lon', models.FloatField()),
                ('last_modified_time', models.DateTimeField()),
                ('archived', models.BooleanField(default=False)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.field')),
            ],
        ),
    ]
