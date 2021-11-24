from django.contrib                    import admin
from django.urls                       import path
from AppReservas                   import views as authViews


urlpatterns = [
    path('verifyToken/',                           authViews.VerifyTokenView.as_view()),
    path('reserva_usuario/',                       authViews.ReservaCreateView.as_view()),
    path('reservas/',                              authViews.AllReservasDetailView.as_view()),
    path('reservas_usuario/<int:user>/',           authViews.AllUserReservasDetailView.as_view()),
    path('reserva_usuario/<int:pk>/',              authViews.ReservaDetailView.as_view()),
    path('reserva_usuario/update/<int:pk>/',       authViews.ReservaUpdateView.as_view()),
    path('transaction/remove/<int:pk>/',           authViews.ReservaDeleteView.as_view()),
    path('plans/',                                 authViews.AllPlansDetailView.as_view()),
    path('plans_for_time/<str:jornada>/',                        authViews.PlanForTimeDetailView.as_view()),
    path('plans_for_price/<int:precio>/',                       authViews.PlanForPriceDetailView.as_view()),
    path('plan_usuario/<int:pk>/',                 authViews.PlanDetailView.as_view()),
    path('plan_usuario/update/<int:pk>/',          authViews.PlanUpdateView.as_view()),
]