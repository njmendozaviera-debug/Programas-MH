import math

def f(x):
    return (x*math.log(x)) - 1
def df(x):
    return math.log(x) + 1


x0 = 1.8 #Semilla inicial
tol = 1e-6 #Tolerancia

for i in range(100):
    x1 = x0 - f(x0)/df(x0) #Formula de Newton-Raphson

    error = abs(x1 - x0)

    if error < tol:
        print(f"Listo, Convergencia alcanzada en {i} iteraciones")
        break

    x0 = x1

print(f"Iteraciones: {i}")
print(f"El valor aproximado de la raiz es: {x1}")
print(f"El valor de f(c) es: ({f(x1)})")