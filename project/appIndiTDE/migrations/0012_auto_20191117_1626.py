# Generated by Django 2.2.6 on 2019-11-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appIndiTDE', '0011_auto_20191116_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sugerencia',
            name='autor',
        ),
        migrations.AddField(
            model_name='sugerencia',
            name='nombre',
            field=models.CharField(default='anonymous', max_length=20),
        ),
    ]
