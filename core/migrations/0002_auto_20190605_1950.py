# Generated by Django 2.2.1 on 2019-06-05 23:50

import core.DurationField
import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtt',
            name='group_size_gap',
            field=core.DurationField.DurationField(default=core.models.duration_field_5m, verbose_name='Group Size Gap'),
        ),
        migrations.AlterField(
            model_name='resultmassstart',
            name='adjustment_time',
            field=core.DurationField.DurationField(blank=True, default=core.models.duration_field_0, null=True, verbose_name='Adjustment Time'),
        ),
        migrations.AlterField(
            model_name='resulttt',
            name='adjustment_time',
            field=core.DurationField.DurationField(blank=True, default=core.models.duration_field_0, null=True, verbose_name='Adjustment Time'),
        ),
        migrations.AlterField(
            model_name='wave',
            name='start_offset',
            field=core.DurationField.DurationField(default=core.models.duration_field_0, verbose_name='Start Offset'),
        ),
        migrations.AlterField(
            model_name='wavett',
            name='fastest_participants_start_gap',
            field=core.DurationField.DurationField(default=core.models.duration_field_2m, verbose_name='Fastest Participants Start Gap'),
        ),
        migrations.AlterField(
            model_name='wavett',
            name='gap_before_wave',
            field=core.DurationField.DurationField(default=core.models.duration_field_5m, verbose_name='Gap Before Wave'),
        ),
        migrations.AlterField(
            model_name='wavett',
            name='regular_start_gap',
            field=core.DurationField.DurationField(default=core.models.duration_field_1m, verbose_name='Regular Start Gap'),
        ),
    ]