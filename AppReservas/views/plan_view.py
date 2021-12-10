from django.conf                         import settings
from rest_framework                      import generics

from AppReservas.models.plan_usuario              import Plan_usuario
from AppReservas.serializers.plan_serializer       import PlanSerializer


class PlanDetailView(generics.RetrieveAPIView):
    queryset            = Plan_usuario.objects.all()
    serializer_class    = PlanSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

class AllPlansDetailView(generics.ListAPIView):
    queryset            = Plan_usuario.objects.all()
    serializer_class    = PlanSerializer

#Get Plans depending on the day
class PlanForTimeDetailView(generics.ListAPIView):
    queryset            = Plan_usuario.objects.all()
    serializer_class    = PlanSerializer
    def get_queryset(self):
        queryset = Plan_usuario.objects.filter(jornada=self.kwargs["jornada"])
        return queryset

#Get Plans for price
class PlanForPriceDetailView(generics.ListAPIView):
    queryset            = Plan_usuario.objects.all()
    serializer_class    = PlanSerializer
    def get_queryset(self):
        queryset = Plan_usuario.objects.filter(precio=self.kwargs["precio"])
        return queryset 

class PlanUpdateView(generics.UpdateAPIView):
    queryset         = Plan_usuario.objects.all()
    serializer_class = PlanSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class PlanDeleteView(generics.DestroyAPIView):
    queryset         = Plan_usuario.objects.all()
    serializer_class = PlanSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)