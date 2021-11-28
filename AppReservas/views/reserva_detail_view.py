""" las vistas del modelo de la reserva usuario, la clase ReservaDetailView es para ver una reserva en especifico, 
AllReservasDetailView es para ver todas las reservas, AllUserReservasDetailView es para ver las reservas de un usuario
segun el numero de documento de identidad, ReservaUpdateView editar una  reserva y el ReservaDeleteView para eliminar 
una reserva"""

from django.conf                         import settings
from rest_framework                      import generics, status

from AppReservas.models.reserva_usuario import Reserva
from AppReservas.serializers.reserva_serializer import ReservaSerializer

class ReservaDetailView(generics.RetrieveAPIView):
    queryset            = Reserva.objects.all()
    serializer_class    = ReservaSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

class AllReservasDetailView(generics.ListAPIView):
    queryset         = Reserva.objects.all()
    serializer_class = ReservaSerializer

class AllUserReservasDetailView(generics.ListAPIView):
    queryset         = Reserva.objects.all()
    serializer_class = ReservaSerializer  
    def get_queryset(self):
        queryset = Reserva.objects.filter(numero_documento=self.kwargs["user"])
        return queryset

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