# Generated by Django 4.0.2 on 2022-03-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm_en', models.CharField(default='', max_length=64)),
                ('dorm_ko', models.CharField(default='', max_length=64)),
                ('boy', models.BooleanField(default=True)),
            ],
        ),
    ]
