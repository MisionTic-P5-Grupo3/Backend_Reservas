from django.db    import models



JORNADAS = (("Diurno","diurno"),("Nocturno","nocturno"))
class Plan_usuario(models.Model): 
    id_plan            = models.AutoField(primary_key=True)
    jornada            = models.CharField('Jornada',choices=JORNADAS, max_length=10, default="Diurno")
    nombre_plan        = models.CharField('Nombre del plan', max_length=50)
    descripcion        = models.CharField('Nombre del plan', max_length=100)
    precio             = models.FloatField('Precio', default= 0.00)
    url                = models.CharField('Nombre del plan', max_length=2083, default="https://elcomercio.pe/resizer/TGCsuHf4e88fBOhhEUbfaHgHs9A=/560x0/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/ZPAAAE7JYRBETISIFG3E77ZACU.png")
    
