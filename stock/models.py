import datetime

from django.db import models

# Create your models here.
class StockCategory(models.Model):
    category_name = models.CharField(max_length=200)


class Client(object):
    pass


class Stock(models.Model):
    stock_name = models.CharField(max_length=200)
    stock_category = models.CharField(max_length=200)
    purchase_price = models.CharField(max_length=200)
    #stock_category=models.ForeignKey(StockCategories, null=True, blank=True, on_delete=models.CASCADE)
    date_purchased = models.CharField(max_length=200,default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    client_id = models.CharField(max_length=200)
    #client_id = models.ForeignKey(Clients, null=True, blank=True, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    stock_unit = models.CharField(max_length=200)
    selling_price_per_unit = models.IntegerField()



