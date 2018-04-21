from django.db import models

# Create your models here.

class Delivery_product(models.Model):
    id_product= models.IntegerField()
    id_trasanction= models.IntegerField()
    quality= models.IntegerField()
    state= models.IntegerField()
    date= models.DateTimeField(auto_now_add=True)


    def __string__(self):
        return (self.id_product
                + "\nTransaction: " + self.id_trasanction
                + "\nQuality: " + self.quality
                + "\nState: " + self.state
                + "\nDate: " + self.date
                )
