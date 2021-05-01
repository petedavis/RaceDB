# Generated by Django 2.2.9 on 2020-05-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200519_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='systeminfo',
            name='date_Md',
            field=models.CharField(default='M d', max_length=24, verbose_name='Month Day Format'),
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='date_short',
            field=models.CharField(default='Y-m-d', max_length=24, verbose_name='Date Short Format'),
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='time_hhmmss',
            field=models.CharField(default='H:i:s', max_length=24, verbose_name='Time Short Format'),
        ),
        migrations.AlterField(
            model_name='wavett',
            name='sequence_option',
            field=models.PositiveSmallIntegerField(choices=[('Increasing', ((0, 'Est. Speed - Increasing'), (1, 'Youngest to Oldest'), (2, 'Bib - Increasing'))), ('Decreasing', ((6, 'Est. Speed - Decreasing'), (3, 'Oldest to Youngest'), (4, 'Bib - Decreasing'))), ('Series', ((5, 'Series Rank'),))], default=0, help_text='Criteria used to order participants in the wave', verbose_name='Sequence Option'),
        ),
    ]