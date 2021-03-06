# Generated by Django 4.0.2 on 2022-03-25 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='degree',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.degree', verbose_name='학위과정'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dormitory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.dormitory', verbose_name='기숙사'),
        ),
    ]
