# Generated by Django 3.2.3 on 2021-05-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20210516_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduation_year',
            field=models.IntegerField(),
        ),
    ]
