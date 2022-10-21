# Generated by Django 4.1.1 on 2022-10-21 11:29

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
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webpage.funcionario'),
        ),
    ]