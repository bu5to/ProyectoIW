# Generated by Django 2.2.8 on 2019-12-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appIndiTDE', '0014_ropa_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='descEn',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
