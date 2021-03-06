# Generated by Django 2.0 on 2018-05-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=200)),
                ('purchase_price', models.CharField(max_length=200)),
                ('stock_category', models.CharField(max_length=200)),
                ('date_purchased', models.CharField(default='2018-05-25 14:58:11', max_length=200)),
                ('client_id', models.CharField(max_length=200)),
                ('stock_quantity', models.IntegerField()),
                ('stock_unit', models.CharField(max_length=200)),
                ('selling_price_per_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StockCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
    ]
