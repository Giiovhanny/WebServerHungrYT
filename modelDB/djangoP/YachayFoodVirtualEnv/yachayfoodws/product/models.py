# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#from customer.customer import Customer

class Product(models.Model):
    id_product = models.IntegerField(primary_key=True)
    id_seller = models.ForeignKey('customer.Customer', models.DO_NOTHING, db_column='id_seller', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    limit_date = models.DateTimeField(blank=True, null=True)
    register_date = models.DateField(blank=True, null=True)
    id_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

    #def __str__(self):
    #    return self.product
