# Generated by Django 4.0.3 on 2022-04-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_usercart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
