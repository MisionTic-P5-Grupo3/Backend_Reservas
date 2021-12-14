from django.db                     import models
from .plan_usuario                 import Plan_usuario

class Reserva(models.Model):
    id_reserva = models.BigAutoField(primary_key=True)
    tipo_documento = models.CharField('Tipo de documento', max_length=20)
    numero_documento = models.FloatField('Numero de documento', max_length=20)
    nombre_completo = models.CharField('Nombre completo', max_length=50)
    telefono = models.CharField('Numero de Telefono', max_length=15)
    correo_electronico = models.EmailField('Correo', max_length=100)
    fecha = models.DateField('Fecha', max_length=50)
    id_plan = models.ForeignKey(Plan_usuario,related_name='plan_usuario', on_delete=models.CASCADE)



