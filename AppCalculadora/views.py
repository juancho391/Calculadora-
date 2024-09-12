from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home(request):
    return render(request, 'index.html')




class ControladorCalculadora(APIView):
    def post(self, request):
        listaNumeros = request.data.get('ListaExpresion', [])

        # Verifica que listaNumeros sea una lista y contenga exactamente 3 elementos
        if not isinstance(listaNumeros, list) or len(listaNumeros) != 3:
            return Response({"error": "Expresión no válida. Debe contener exactamente dos números y un operador."}, status=400)

        operador = listaNumeros[1]

        try:
            num1 = float(listaNumeros[0])
            num2 = float(listaNumeros[2])
        except (ValueError, TypeError):
            return Response({"error": "Uno o más valores no son números válidos."}, status=400)

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                return Response({"error": "División por cero."}, status=400)
            resultado = num1 / num2
        elif operador == "^":
            resultado = num1 ** num2
        elif operador == "√":
            if num1 < 0 and num2 % 2 == 0:
                return Response({"error": "Raíz cuadrada de un número negativo."}, status=400)
            resultado = num1 ** (1 / num2)
        else:
            return Response({"error": "Operador no válido."}, status=400)

        return Response({"resultado": resultado})



            


