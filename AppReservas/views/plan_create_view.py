from rest_framework                                  import serializers, status, views
from rest_framework.response                         import Response
from rest_framework_simplejwt.serializers            import TokenObtainPairSerializer
from AppReservas.serializers.plan_serializer         import CreatePlanSerializer, PlanSerializer

class PlanCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreatePlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializers_mostrar = PlanSerializer(data = serializer.data) 
        serializers_mostrar.is_valid()
        return Response(serializers_mostrar.data)