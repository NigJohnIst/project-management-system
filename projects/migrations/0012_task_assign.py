# Generated by Django 2.0.3 on 2018-03-30 19:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0011_auto_20180330_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assign',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]