# Generated by Django 3.0.4 on 2020-04-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_place_placestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
