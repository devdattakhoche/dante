# Generated by Django 2.2.5 on 2019-10-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20191028_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='place',
            field=models.CharField(choices=[('Auditorium', 'Auditorium'), ('Place2', 'Place2'), ('Place3', 'Place3')], default='Pending', max_length=100),
        ),
    ]
