import math

def f(x):
    return math.exp(-x) - x

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tol = 1e-6 # Tolerancia de la convergencia
error = 1.0 #arrancamos alto error
c_anterior = a #para calcular el error luego


for i in range(100): 
    c = (a + b) / 2 #punto medio

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    error = abs(c - c_anterior)
    c_anterior = c


    if error < tol:
        print(f"Listo, Convergencia alcanzada en {i} iteraciones")
        break

    
print(f"Iteraciones: {i}")
print(f"El valor aproximado de la raiz es: {c}")
print(f"El valor de f(c) es: ({f(c)})")
