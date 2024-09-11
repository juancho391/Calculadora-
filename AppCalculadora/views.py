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
    

class Resta(APIView):
    def post(self, request):
        # Obtenemos la lista de números que llega en el JSON
        listaNumeros = request.data.get('listaNumeros')
        
        # Validamos que haya llegado una lista de numeros
        if not listaNumeros or not isinstance(listaNumeros, list):
            return Response({'error': 'Debes proporcionar una lista de números.'}, status=400)

        # Calculamos la resta de los numeros en la lista
        resultado = listaNumeros[0]  # Comenzamos con el primer numero
        for numero in listaNumeros[1:]:
            resultado -= numero  # Restamos cada numero siguiente
        
        # Devolvemos la respuesta con el resultado de la resta
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
    

class Division(APIView):
    def post(self, request):
        # Obtenemos la lista de números que llegó en el JSON
        listaNumeros = request.data.get('listaNumeros')

        # Inicializamos el resultado con el primer número de la lista
        resultado = listaNumeros[0]

        # Iteramos desde el segundo número en adelante y dividimos el resultado
        for numero in listaNumeros[1:]:
            if numero != 0:
                resultado /= numero
            else:
                return Response({'error': 'Indefinido'}, status=400) #Error 400 la solicitud del usuario tiene algun error

        return Response({'resultado': resultado})

class Raiz(APIView):
    def post(self, request):
        # Obtenemos el número y el índice de la raíz que se quiere calcular
        numero = request.data.get('numero')
        raiz = request.data.get('raiz')

        # Validamos que no se intente calcular la raíz 0
        if raiz == 0:
            return Response({'error': 'El índice de la raíz no puede ser 0'}, status=400)
        
        # Calculamos la raíz usando el operador **
        resultado = numero ** (1 / raiz)
        
        # Devolvemos el resultado de la raíz
        return Response({'resultado_raiz': resultado})

class Potencia(APIView):
    def post(self, request):
        # Obtenemos el número base y la potencia
        base = request.data.get('base')
        exponente = request.data.get('exponente')
        
        # Calculamos la base elevada a la potencia usando el operador **
        resultado = base ** exponente
        
        # Devolvemos el resultado de la operación
        return Response({'resultado_potencia': resultado})


