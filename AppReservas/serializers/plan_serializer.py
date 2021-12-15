from AppReservas.models.plan_usuario import Plan_usuario
from rest_framework import serializers

class CreatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan_usuario
        fields = ['id_plan','jornada','nombre_plan','descripcion','precio','url']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan_usuario
        fields =  ['id_plan','jornada','nombre_plan','descripcion','precio'] #campos obligatorios para la creacion del objeto

    def to_representation(self, obj):
        planData = Plan_usuario.objects.get(id_plan=obj.id_plan)
        return {
            'id_plan' : planData.id_plan,
            'nombre_plan' : planData.nombre_plan,
            'jornada'     : planData.jornada,
            'descripcion' : planData.descripcion,
            'precio'      : planData.precio,
            'url': planData.url
        }