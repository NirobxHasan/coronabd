# Generated by Django 3.0.4 on 2020-04-16 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20200416_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='district',
            new_name='city',
        ),
    ]
