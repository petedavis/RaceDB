# Generated by Django 4.2 on 2023-05-24 20:07

import core.DurationField
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_series_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeTT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effort', models.PositiveSmallIntegerField(choices=[(0, 'Pack'), (1, 'Break'), (2, 'Chase'), (-1, 'Custom')], default=0, verbose_name='Effort')),
                ('effort_custom', models.CharField(blank=True, default='', max_length=36, verbose_name='Effort Custom')),
                ('position', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Position')),
                ('laps_to_go', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Laps to Go')),
                ('sponser', models.CharField(blank=True, default='', max_length=80, verbose_name='Sponser')),
                ('cash', models.FloatField(default=None, null=True, verbose_name='Cash')),
                ('merchandise', models.CharField(blank=True, default='', max_length=64, verbose_name='Merchandise')),
                ('points', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Points')),
                ('time_bonus', core.DurationField.DurationField(default=None, null=True, verbose_name='Time Bonus')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.eventtt')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.participant')),
            ],
            options={
                'verbose_name': 'PrimeTT',
                'verbose_name_plural': 'PrimesTT',
                'ordering': ['-laps_to_go', 'position', 'participant__bib'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrimeMassStart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effort', models.PositiveSmallIntegerField(choices=[(0, 'Pack'), (1, 'Break'), (2, 'Chase'), (-1, 'Custom')], default=0, verbose_name='Effort')),
                ('effort_custom', models.CharField(blank=True, default='', max_length=36, verbose_name='Effort Custom')),
                ('position', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Position')),
                ('laps_to_go', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Laps to Go')),
                ('sponser', models.CharField(blank=True, default='', max_length=80, verbose_name='Sponser')),
                ('cash', models.FloatField(default=None, null=True, verbose_name='Cash')),
                ('merchandise', models.CharField(blank=True, default='', max_length=64, verbose_name='Merchandise')),
                ('points', models.PositiveSmallIntegerField(default=None, null=True, verbose_name='Points')),
                ('time_bonus', core.DurationField.DurationField(default=None, null=True, verbose_name='Time Bonus')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.eventmassstart')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.participant')),
            ],
            options={
                'verbose_name': 'PrimeMassStart',
                'verbose_name_plural': 'PrimesMassStart',
                'ordering': ['-laps_to_go', 'position', 'participant__bib'],
                'abstract': False,
            },
        ),
    ]