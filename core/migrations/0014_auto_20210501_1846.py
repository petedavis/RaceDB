# Generated by Django 3.2 on 2021-05-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210501_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultmassstart',
            name='category_gap',
            field=models.CharField(blank=True, default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='resulttt',
            name='category_gap',
            field=models.CharField(blank=True, default='', max_length=24),
        ),
    ]