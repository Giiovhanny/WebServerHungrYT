# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Indent(models.Model):
    id_indent = models.IntegerField(unique=True, blank=True, null=True)
    id_cart = models.ForeignKey('shoppingCart.ShoppingCart', models.DO_NOTHING, db_column='id_cart', blank=True, null=True)
    id_product = models.ForeignKey('product.Product', models.DO_NOTHING, db_column='id_product', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indent'
