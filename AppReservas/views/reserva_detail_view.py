from django.conf                         import settings
from rest_framework                      import generics, status

from AppReservas.models.reserva_usuario import Reserva
from AppReservas.serializers.reserva_serializer import ReservaSerializer

class ReservaDetailView(generics.RetrieveAPIView):
    queryset            = Reserva.objects.all()
    serializer_class    = ReservaSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class ReservaUpdateView(generics.UpdateAPIView):
    queryset         = Reserva.objects.all()
    serializer_class = ReservaSerializer
    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)


class ReservaDeleteView(generics.DestroyAPIView):
    queryset         = Reserva.objects.all()
    serializer_class = ReservaSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)