from django.db import models
from django.conf import settings

# Create your models here.


class Contacto(models.Model):
    nombre=models.CharField(max_length=40)
    mail=models.EmailField()
    tel=models.IntegerField()
    comentario=models.TextField()


    def __str__(self):
        return f'{self.nombre} - {self.mail}'


class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    mail=models.EmailField()
    tel=models.IntegerField()
    metodo_de_pago_choices=(
        ('Tarjeta de Credito','Tarjeta de Credito'),
        ('Tarjeta de Debito','Tarjeta de Debito'),
        ('Mercado Pago','Mercado Pago'),
        ('Transferencia','Transferencia'),
        ('Cheque','Cheque'),
        ('Efectivo','Efectivo')
    )
    metodo_de_pago=models.CharField(max_length=20, choices=metodo_de_pago_choices,default='Tarjeta de Debito')

    def __str__(self):
        return f'{self.nombre} - {self.mail}'


class Empleado(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)



class Producto(models.Model):
    nombre_producto=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    imagen=models.ImageField(upload_to='productos',null=True,blank=True)
    empleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_producto} - {self.empleado}'
    

