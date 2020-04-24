# Generated by Django 3.0.4 on 2020-04-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20200416_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='location',
        ),
        migrations.AddField(
            model_name='area',
            name='name',
            field=models.CharField(blank=True, max_length=220, unique=True),
        ),
    ]
