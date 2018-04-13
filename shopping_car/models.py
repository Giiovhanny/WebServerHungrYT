from django.db import models

# Creation of class products
class Shopping_Car(models.Model):
    id_car = models.IntegerField(primary_key=True, max_length=4)        #id_car      int(4)
    id_buyer = models.IntegerField(max_length=4)                        #id_buyer    int(4)
    direction = models.CharField(max_length=255)                        #direction   varchar(255)