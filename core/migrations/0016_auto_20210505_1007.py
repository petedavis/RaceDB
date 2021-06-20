# Generated by Django 3.2 on 2021-05-05 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_participant_bib'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventmassstart',
            options={'ordering': ['date_time'], 'verbose_name': 'Mass Start Event', 'verbose_name_plural': 'Mass Starts Event'},
        ),
        migrations.AlterModelOptions(
            name='racetimemassstart',
            options={'ordering': ['race_time'], 'verbose_name': 'RaceTimeMassStart', 'verbose_name_plural': 'RaceTimesMassStart'},
        ),
        migrations.AlterModelOptions(
            name='racetimett',
            options={'ordering': ['race_time'], 'verbose_name': 'RaceTimeTT', 'verbose_name_plural': 'RaceTimesTT'},
        ),
        migrations.AlterModelOptions(
            name='resultmassstart',
            options={'ordering': ['status', 'wave_rank'], 'verbose_name': 'ResultMassStart', 'verbose_name_plural': 'ResultsMassStart'},
        ),
        migrations.AlterModelOptions(
            name='resulttt',
            options={'ordering': ['status', 'wave_rank'], 'verbose_name': 'ResultTT', 'verbose_name_plural': 'ResultsTT'},
        ),
    ]