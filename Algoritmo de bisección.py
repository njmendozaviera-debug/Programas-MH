import math

def f(x):
    return math.exp(-x) - x

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tol = 1e-6 # Tolerancia de la convergencia

# Aplicamos el teorema de bolzano para verificar la raiz
if f(a) * f(b) > 0:
    print("Error. El teorema de Bolzano no se cumple en este intervalo.")
    print("f(a) y f(b) tienen el mismo signo, por lo que no se garantiza una raiz (o hay numero par de ellas).")
else:
    print("El teorema de Bolzano se cumple. Procediendo con el calculo...")

    error = 1.0 #arrancamos alto error
    c_anterior = a #para calcular el error luego
    c = a #Iniciamos c por si acaso

    for i in range(100): 
        c = (a + b) / 2 #punto medio

        #Verificamos si encontramos la raiz exacta por casualidad
        if f(c) == 0:
            print(f"Raíz exacta encontrada exactamente en la iteracion: {i}")
            break
        
        #Seleccion del subintervalo segun el cambio de signo
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