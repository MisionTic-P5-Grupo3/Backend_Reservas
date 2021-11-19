from django.conf                         import settings
from rest_framework                      import generics, status

from AppReservas.models.plan_usuario              import Plan_usuario
from AppReservas.serializers.plan_serializer       import PlanSerializer

class PlanDetailView(generics.RetrieveAPIView):
    queryset            = Plan_usuario.objects.all()
    serializer_class    = PlanSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

class PlanUpdateView(generics.UpdateAPIView):
    queryset         = Plan_usuario.objects.all()
    serializer_class = PlanSerializer
    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)


class PlanDeleteView(generics.DestroyAPIView):
    queryset         = Plan_usuario.objects.all()
    serializer_class = PlanSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)