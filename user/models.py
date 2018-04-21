from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre ')
    last_name = models.CharField(max_length=30, verbose_name='Apellido ')
    email = models.CharField(max_length=50, verbose_name='Email ')
    user_name= models.CharField(max_length=15, verbose_name= 'Nombre de Usuario ')
    password=models.CharField(max_length=10)
    cellphone= models.CharField(max_length=10, verbose_name= 'Celular ')
    is_seller= models.BooleanField(verbose_name= 'Vendedor')
    direction= models.TextField(max_length= 255, verbose_name= 'Direccion ')
    
    def __string__(self):
        return (self.name
                + "\nLast_Name: " + self.last_name
                + "\nEmail: " + self.email
                + "\nUser_Name: " + self.user_name
                + "\nPassword: " +self.password
                + "\nCellphone: "+ self.cellphone
                + "\nSeller: " +self.is_seller
                + "\nDirection: " + self.direction
                )