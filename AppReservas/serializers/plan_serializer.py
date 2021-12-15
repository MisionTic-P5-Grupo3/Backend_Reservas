from AppReservas.models.plan_usuario import Plan_usuario
from rest_framework import serializers

class CreatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan_usuario
        fields = ['id_plan','jornada','nombre_plan','descripcion','precio','url']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan_usuario
        fields =  ['id_plan','jornada','nombre_plan','descripcion','precio','url'] #campos obligatorios para la creacion del objeto
