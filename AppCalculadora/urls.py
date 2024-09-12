from django.urls import path
from .views import ControladorCalculadora



urlpatterns = [
   path('calculadora/', ControladorCalculadora.as_view()),
]
