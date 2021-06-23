# Generated by Django 3.0.5 on 2021-06-17 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order_pizza', '0002_auto_20210617_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='timestamps',
        ),
        migrations.AddField(
            model_name='product',
            name='timeStamps',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
