from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Suma(APIView):
    def post(self, request):
        # Obtenemos la lista de numeros que llego en el json 
        listaNumeros = request.data.get('listaNumeros')
        
        # Calculamos la suma de todos los numeros en la lista
        resultado = sum(listaNumeros)
        
        # Devuelve la respuesta con el resultado de la suma
        return Response({'resultado': resultado})
    

