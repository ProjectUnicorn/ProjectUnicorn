# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-05 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('applicationlist', '0002_auto_20171004_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=100, verbose_name='Klassifikation')),
            ],
        ),
        migrations.CreateModel(
            name='ClassificationColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='applicationContainsPersonData',
            field=models.BooleanField(default=False, verbose_name='Persondata'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicationDataDeal',
            field=models.URLField(blank=True, max_length=255, verbose_name='Data aftale'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicationRiskEvaluation',
            field=models.URLField(blank=True, max_length=255, verbose_name='Risikovurdering'),
        ),
        migrations.AddField(
            model_name='classification',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicationlist.ClassificationColor', verbose_name='Farve'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicationClassification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='applicationlist.Classification', verbose_name='Klassifikation'),
        ),
    ]
