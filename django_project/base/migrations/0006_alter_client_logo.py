# Generated by Django 3.2.3 on 2021-07-28 12:41

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210707_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(null=True, upload_to=base.models.upload_client_image),
        ),
    ]
