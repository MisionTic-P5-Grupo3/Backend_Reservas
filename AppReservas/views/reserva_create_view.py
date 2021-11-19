from rest_framework                                  import status, views
from rest_framework.response                         import Response
from rest_framework_simplejwt.serializers            import TokenObtainPairSerializer
from AppReservas.serializers.reserva_serializer   import ReservaSerializer


class ReservaCreateView(views.APIView):
        def post(self, request, *args, **kwargs):
                serializer = ReservaSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            
                return Response(serializer.validated_data)