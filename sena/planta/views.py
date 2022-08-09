from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'planta/index.html')

""" 

def saludar(request):
    return HttpResponse("Hola <strong>mundo</strong>!<br/><a href='/planta/comprar/'>Comprar</a>")

def comprar(request):
    return HttpResponse("Compraste!!<br/><a href='/planta/saludo/'>Ir al principio</a>")

def saludoEspecial(request, dato):
    return HttpResponse(f"hola {dato}")

def sumarDosNum(request, num1, num2):
    r = num1 + num2
    return HttpResponse(f"Resultado de {num1} + {num2} = {r}")


def loginFormulario(request):
    return render(request, 'planta/login/login-form.html')

def login(request):
    u = request.POST["usuario"]
    c = request.POST["clave"]
    
    if u == "jor" and c == "12345":
        return HttpResponse("Bienvenido!!")
    else:
        return HttpResponse("Usuario o contraseña incorrectos...")
    
def calcFormulario(request):
    return render(request, 'planta/calc/calc-form.html')

def calc(request):
    num1 = request.POST["num1"]
    num2 = request.POST["num2"]
    
    r = int(num1) + int(num2)
    return HttpResponse(f"La suma de:  {num1} + {num2} = <strong style='color:red;'>{r}</strong>") """
    



    