# Generated by Django 4.0.2 on 2022-03-20 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_frienddecision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frienddecision',
            old_name='receiver_id',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='frienddecision',
            old_name='sender_id',
            new_name='sender',
        ),
    ]