from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre=models.CharField(max_length=40)
    mail=models.EmailField()
    tel=models.IntegerField()
    comentario=models.TextField()


    def __str__(self):
        return f'{self.nombre} - {self.mail}'

