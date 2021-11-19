from AppReservas.models.reserva_usuario import Reserva
from AppReservas.models.plan_usuario    import Plan_usuario
from AppReservas.serializers.plan_serializer import PlanSerializer
from rest_framework                     import serializers


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'tipo_documento','numero_documento','nombre_completo','telefono','correo_electronico','fecha','id_plan']
      
        def to_representation(self, obj):#no se quita para que no se retornen todos los campos
            reserva = Reserva.objects.get(id_reserva=obj.id_reserva)
            plan = Plan_usuario.objects.get(id_plan=obj.id_plan_id)
           
          
             
            return { #informacion que llega al frontend 
                'id_reserva' : reserva.id_reserva,
                'id_tipo_documento' : reserva.id_tipo_documento,
                'numero_documento': reserva.numero_documento, 
                'nombre_completo': reserva.nombre_completo,
                'telefono': reserva.telefono,
                'correo_electronico': reserva.correo_electronico,
                'fecha': reserva.fecha,
                'id_plan':{
                    'nombre_plan': plan.nombre_plan,
                    'precio':plan.precio, 
                }
            }