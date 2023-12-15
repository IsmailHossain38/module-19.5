# Generated by Django 5.0 on 2023-12-10 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='musicians',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musician.musician'),
        ),
    ]
