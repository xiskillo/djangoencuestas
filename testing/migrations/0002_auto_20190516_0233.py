# Generated by Django 2.2.1 on 2019-05-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CLOSED', 'Closed')], default='pending', max_length=155),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]