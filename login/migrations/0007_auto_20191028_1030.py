# Generated by Django 2.2.6 on 2019-10-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20191028_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='userid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
