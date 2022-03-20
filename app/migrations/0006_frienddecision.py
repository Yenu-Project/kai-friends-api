# Generated by Django 4.0.2 on 2022-03-20 12:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_dormitory'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성 시간')),
                ('finalized_at', models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0, tzinfo=utc), verbose_name='신청 받은 사람의 결정 시간')),
                ('receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_decisions', to=settings.AUTH_USER_MODEL, verbose_name='받은 사람')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_decisions', to=settings.AUTH_USER_MODEL, verbose_name='보낸 사람')),
            ],
        ),
    ]
