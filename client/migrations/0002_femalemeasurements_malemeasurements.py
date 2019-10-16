"""Migrations for measurements."""
# Generated by Django 2.2.6 on 2019-10-15 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """Measurments model mapping on table."""

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaleMeasurements',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('unit', models.CharField(choices=[
                 ('cm', 'Centimetre'), ('inc', 'Inches')], default='inc',
                                        max_length=3)),
                ('shoulder', models.PositiveSmallIntegerField()),
                ('armscye', models.PositiveSmallIntegerField()),
                ('chest', models.PositiveSmallIntegerField()),
                ('bust', models.PositiveSmallIntegerField()),
                ('waist', models.PositiveSmallIntegerField()),
                ('arm_length', models.PositiveSmallIntegerField()),
                ('hips', models.PositiveSmallIntegerField()),
                ('ankle', models.PositiveSmallIntegerField()),
                ('neck', models.PositiveSmallIntegerField()),
                ('back_width', models.PositiveSmallIntegerField()),
                ('inseam', models.PositiveSmallIntegerField()),
                ('wrist', models.PositiveSmallIntegerField()),
                ('crutch_depth',
                 models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_knee',
                 models.PositiveSmallIntegerField(blank=True)),
                ('knee_line', models.PositiveSmallIntegerField(blank=True)),
                ('biceps', models.PositiveSmallIntegerField(blank=True)),
                ('client', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='client.Client')),
            ],
        ),
        migrations.CreateModel(
            name='FemaleMeasurements',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('unit', models.CharField(choices=[
                 ('cm', 'Centimetre'), ('inc', 'Inches')], default='inc',
                                        max_length=3)),
                ('shoulder', models.PositiveSmallIntegerField()),
                ('chest', models.PositiveSmallIntegerField()),
                ('waist', models.PositiveSmallIntegerField()),
                ('hips', models.PositiveSmallIntegerField()),
                ('armscye', models.PositiveSmallIntegerField()),
                ('bust', models.PositiveSmallIntegerField()),
                ('arm_length', models.PositiveSmallIntegerField()),
                ('ankle', models.PositiveSmallIntegerField()),
                ('neck', models.PositiveSmallIntegerField()),
                ('back_width', models.PositiveSmallIntegerField()),
                ('inseam', models.PositiveSmallIntegerField()),
                ('wrist', models.PositiveSmallIntegerField()),
                ('front_sh_to_waist',
                 models.PositiveSmallIntegerField(blank=True)),
                ('crutch_depth',
                 models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_knee',
                 models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_hip',
                 models.PositiveSmallIntegerField(blank=True)),
                ('knee_line', models.PositiveSmallIntegerField(blank=True)),
                ('top_arm', models.PositiveSmallIntegerField(blank=True)),
                ('body_rise', models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_floor',
                 models.PositiveSmallIntegerField(blank=True)),
                ('client', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='client.Client')),
            ],
        ),
    ]
