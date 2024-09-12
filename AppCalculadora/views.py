from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ControladorCalculadora(APIView):
    def post(self, request):
        listaNumeros = request.data.get('listaNumeros')
        #verifico si la lista contiene 2 numeros y el operador
        if len(listaNumeros) == 3:
            #verifico que el operador sea +
            if "+" in listaNumeros:
                for i in listaNumeros:
                    #sumo los numeros suponiendo que el operador esta en la posicion 1
                    suma = listaNumeros[0] + listaNumeros[2]
                    return Response({"resultado": suma})
            #verifico que el operador sea -
            elif "-" in listaNumeros:
                for i in listaNumeros:
                    #resto los numeros suponiendo que el operador esta en la posicion 1
                    resta = listaNumeros[0] - listaNumeros[2]
                    return Response({"resultado": resta})
            

