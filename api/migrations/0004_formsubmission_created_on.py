# Generated by Django 2.2.2 on 2019-06-17 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190615_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
