# Generated by Django 4.0.2 on 2022-05-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_userprofile_id_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frienddecision',
            name='receiver_decision',
            field=models.BooleanField(default=False, verbose_name='친구 신청 수락 여부'),
        ),
        migrations.AlterField(
            model_name='frienddecision',
            name='sender_decision',
            field=models.BooleanField(default=False, verbose_name='친구 신청 여부'),
        ),
    ]
