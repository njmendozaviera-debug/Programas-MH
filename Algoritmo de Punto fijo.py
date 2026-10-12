import math

def  g(x):
    return math.exp(-1/x)

x0 =1.8 #Valor inicial suministrado por el profesor
tol = 1e-6 #Tolerancia

for i in range(100):
    x1 = g(x0)
    
    error = abs(x1 - x0)
    
    if error < tol:
        print(f"Convergencia alcanzada en {i} iteraciones")
        break
    
    x0 = x1

print(f"Iteraciones: {i}")
print(f"El valor aproximado de la raiz es: {x1}")
print(f"El valor de g({x1}) es: ({g(x1)})")