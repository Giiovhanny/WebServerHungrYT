from django.db import models

# Create your models here.

class Transaction (models.Model):
    id_buyer= models.IntegerField()
    direction= models.TextField(max_length= 255, verbose_name= 'Direccion ')

    def __string__(self):
        return (self.id_buyer
                + "\nDirection: " + self.direction
                )