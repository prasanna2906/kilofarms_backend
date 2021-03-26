from django.db import models

class Product(models.Model):
    id= models.IntegerField(primary_key = True)
    sku_name = models.CharField(max_length=200)
    sku_category = models.CharField(max_length=200)
    price = models.IntegerField()
