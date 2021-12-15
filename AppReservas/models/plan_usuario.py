from django.db    import models

JORNADAS = (("Diurno","diurno"),("Nocturno","nocturno"))
class Plan_usuario(models.Model): 
    id_plan            = models.AutoField(primary_key=True)
    jornada            = models.CharField('Jornada',choices=JORNADAS, max_length=10, default="Diurno")
    nombre_plan        = models.CharField('Nombre del plan', max_length=50)
    descripcion        = models.CharField('Descripcion', max_length=100)
    precio             = models.FloatField('Precio', default= 0.00)
    url                = models.CharField('url', max_length=100)
    
