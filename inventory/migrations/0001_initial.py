# Generated by Django 4.0.3 on 2022-04-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemMain',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=25)),
                ('composition', models.TextField()),
                ('manufacturingdate', models.DateField()),
                ('expirydate', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=25)),
                ('slug', models.SlugField(default='', editable=False, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.itemscat')),
            ],
        ),
    ]