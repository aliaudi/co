# Generated by Django 4.2 on 2023-04-27 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_slug_adddrug_sluga_remove_adddrug_pricee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddrug',
            name='date_of_entering',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 27, 11, 47, 48, 144844)),
        ),
    ]
