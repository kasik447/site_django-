# Generated by Django 5.0.6 on 2024-07-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
