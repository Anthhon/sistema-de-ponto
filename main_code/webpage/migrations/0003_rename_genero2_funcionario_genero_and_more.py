# Generated by Django 4.1.2 on 2022-10-20 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_delete_teste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='genero2',
            new_name='genero',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='Genero',
        ),
    ]