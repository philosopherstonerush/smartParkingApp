# Generated by Django 2.2 on 2023-09-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carPrice', models.IntegerField()),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carPrice', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('avgCarOccupancy', models.IntegerField()),
            ],
        ),
    ]
