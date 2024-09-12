from django.urls import path
from .views import ControladorCalculadora, home



urlpatterns = [
   path('calculadora/', ControladorCalculadora.as_view()),
]
