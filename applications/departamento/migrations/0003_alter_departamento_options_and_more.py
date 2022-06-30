# Generated by Django 4.0.5 on 2022-06-21 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_name_alter_departamento_shor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['id'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
