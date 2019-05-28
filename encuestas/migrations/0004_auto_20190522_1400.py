# Generated by Django 2.2.1 on 2019-05-22 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encuestas', '0003_testing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedimientos',
            name='fechafin',
        ),
        migrations.AddField(
            model_name='procedimientos',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsable Médico'),
        ),
    ]