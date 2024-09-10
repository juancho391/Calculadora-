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
    
class Multiplicacion(APIView):
    def post(self, request):
        # Obtenemos la lista de números que llegó en el JSON
        listaNumeros = request.data.get('listaNumeros')

        producto = 1
        # Iteramos sobre la lista y multiplicamos cada número al acumulador
        for numero in listaNumeros:
            producto *= numero

        # Devuelve la respuesta con el resultado de la multiplicación
        return Response({'resultado': producto})
    

