#Modules necessaries to create models.py
from django.db import models
from datetime import datetime 
from datetime import date

# Creation of class products
class Product(models.Model):
    id_product = models.IntegerField(primary_key=True, max_length=4)    #id_product     int(4)
    id_seller = models.IntegerField(max_length=4)                       #id_seller      int(4)
    name = models.CharField(max_length=30)                              #name           varchar(30)
    description = models.TextField(max_length=255)                      #description    varchar(255)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=2)     #init_cost      numeric(5,2)
    stock = models.IntegerField(max_length=4)                           #stock          int(4)
    image = models.BinaryField()                                        #image          bytea       Con binary field no he visto como se inserten datos por lo que la persona que desarrolle los campos 
    #image = models.ImageField(upload_to='products_images/%Y/%m/%d')    #image          varchar     externos al models.py(q me toco) podria usar esta segunda opción que si la comprobé en el trabajo anterior.   
    delivery_date = models.DateTimeField(default=datetime.now)          #delivery_date  timestamp
    limit_date = models.DateField(default=date.today)                   #limit_date     date
    register_date = models.DateField(default= date.today)               #register_date  date
    id_seller = models.IntegerField(max_length=4)                       #id_category    int(4)

