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
            #verifico que el operador sea x
            elif "x" in listaNumeros:
                for i in listaNumeros:
                    #multiplico los numeros
                    multiplicacion=listaNumeros[0] * listaNumeros[2]
                    return Response({"resultado": multiplicacion})
            #verifico que el operador sea /
            elif "/" in listaNumeros:
                for i in listaNumeros:
                #Si el segundo numero es diferente a cero dividimos
                    if listaNumeros[2]!=0:
                        division=listaNumeros[0]/listaNumeros[2]
                #Si el segundo numero es 0 es indefinido
                    else:
                         return Response ({"error": "Indefinido"})
                return Response ({"resultado": division})
            elif "^" in listaNumeros:
                for i in listaNumeros:
                 if listaNumeros[1] == "^":
                    Potencia = listaNumeros[0] ** listaNumeros[2]
                 return Response ({"resultado":Potencia})   
            elif "√" in listaNumeros:
                for i in listaNumeros:
                    if listaNumeros[1] > 0:
                        Raiz = listaNumeros[0]**(1/listaNumeros[2])
                    else:
                        return Response ({"Error":"Numero imaginario"})
                return Response({"Resultado":Raiz})               
                #comentario 
                
                print("hi")
                
                    



            

