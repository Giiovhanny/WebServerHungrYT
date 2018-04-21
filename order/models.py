from django.db import models

# Create your models here.

class Order (models.Model):
    id_card= models.IntegerField()
    id_product= models.IntegerField()
    quantity= models.IntegerField()

    def __string__(self):
        return (self.id_card
                + "\nProduct: " + self.id_product
                +"\nQuantity: " + self.quantity
                )
