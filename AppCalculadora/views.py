from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home(request):
    return render(request, 'index.html')




class ControladorCalculadora(APIView):
    def post(self, request):
<<<<<<< HEAD
        print(request.data)
        listaNumeros = request.data.get('ListaExpresion', [])
        print(listaNumeros)
        
        if len(listaNumeros) != 3:
            return Response({"error": "Expresión no válida. Debe contener exactamente dos números y un operador."}, status=400)
        
        operador = listaNumeros[1]
        
        try:
            num1 = float(listaNumeros[0])
            num2 = float(listaNumeros[2])
        except ValueError:
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
=======
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
                    



            

>>>>>>> 01ac987c31aeff60ec67738c204b1e463cc25a46
