from django.urls import path
from .views import Suma, Resta, Multiplicacion



urlpatterns = [
    path('suma/', Suma.as_view()),
    path('resta/', Resta.as_view()),
    path('Multiplicacion/', Multiplicacion.as_view()),
]
