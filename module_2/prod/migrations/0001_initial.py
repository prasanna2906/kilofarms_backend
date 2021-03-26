# Generated by Django 3.1.7 on 2021-03-26 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sku_name', models.CharField(max_length=200)),
                ('sku_category', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]