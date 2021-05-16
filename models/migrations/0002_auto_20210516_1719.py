# Generated by Django 3.2.3 on 2021-05-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='degree_type',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='department_name',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factulty',
            name='professor_name',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade',
            name='grad_level',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='school_name',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='full_name',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='graduation_year',
            field=models.CharField(default=10, max_length=4),
            preserve_default=False,
        ),
    ]
