from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=30, verbose_name= 'Nombre ')
    description= models.TextField(max_length=255, verbose_name= 'Descripcion')

    def __string__(self):
        return (self.name
                + "\nDirection: " + self.description
                )