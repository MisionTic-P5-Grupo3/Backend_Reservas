from django.db    import models


class Plan_usuario(models.Model): 
    id_plan            = models.AutoField(primary_key=True)
    nombre_plan        = models.CharField('Nombre del plan', max_length=20)
    descripcion       = models.CharField('Nombre del plan', max_length=100)
    precio             = models.FloatField('Precio', default= 0.00)
    
