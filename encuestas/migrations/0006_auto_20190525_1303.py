# Generated by Django 2.2.1 on 2019-05-25 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0005_auto_20190525_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuestas',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuestas.Pacientes', verbose_name='Paciente'),
        ),
    ]
