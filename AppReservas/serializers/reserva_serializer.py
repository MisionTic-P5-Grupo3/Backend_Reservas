from AppReservas.models.reserva_usuario       import Reserva
from AppReservas.models.plan_usuario          import Plan_usuario
from AppReservas.serializers.plan_serializer  import PlanSerializer
from rest_framework                           import serializers

class CreateReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'tipo_documento','numero_documento','nombre_completo','telefono','correo_electronico','fecha','id_plan']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'tipo_documento','numero_documento','nombre_completo','telefono','correo_electronico','fecha','id_plan']
    
    def to_representation(self,obj):
        reserva = Reserva.objects.get(id_reserva=obj.id_reserva)
        plan = obj.id_plan #instancia del tipo Plan

        return{
            "id_reserva"        :reserva.id_reserva,
            "tipo_documento"    :reserva.tipo_documento,
            "numero_documento"  :reserva.numero_documento, 
            "nombre_completo"   :reserva.nombre_completo,
            "telefono"          :reserva.telefono,
            "correo_electronico":reserva.correo_electronico,
            "fecha"             :reserva.fecha,
            "id_plan"           :plan.id_plan,
            "nombre_plan"       :plan.nombre_plan,
            "descripcion_plan"  :plan.descripcion
        }