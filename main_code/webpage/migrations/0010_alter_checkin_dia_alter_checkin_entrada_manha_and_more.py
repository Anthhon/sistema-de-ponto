# Generated by Django 4.1.2 on 2022-10-22 02:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0009_alter_funcionario_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='dia',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='entrada_manha',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='entrada_tarde',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webpage.funcionario'),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='saida_manha',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='saida_tarde',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
    ]
