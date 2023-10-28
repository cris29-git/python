import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return x**3 - 2*x**2 + 4

def derivada(x):
    return 3*x**2 - 4*x

def newton_raphson(funcion, derivada, x_inicial, error, max_iter):
    x = x_inicial
    iteraciones_x = [x]  # Almacenar las iteraciones para la gráfica
    for i in range(max_iter):
        x_siguiente = x - funcion(x) / derivada(x)
        error_absoluto = abs(x_siguiente - x)
        iteraciones_x.append(x_siguiente)
        if error_absoluto < error:
            return x_siguiente, i, iteraciones_x
        x = x_siguiente
    return None, max_iter, iteraciones_x

x_inicial = 2
error_deseado = 1e-6
max_iteraciones = 100

raiz, iteraciones, iteraciones_x = newton_raphson(funcion, derivada, x_inicial, error_deseado, max_iteraciones)

if raiz is not None:
    print(f"Raíz encontrada: {raiz}")
    print(f"Iteraciones requeridas: {iteraciones}")
else:
    print("El método no convergió después de un número máximo de iteraciones.")

# Crear un rango de valores para la gráfica
x_valores = np.linspace(-1, 3, 400)
y_valores = funcion(x_valores)

# Graficar la función y las iteraciones
plt.plot(x_valores, y_valores, label="f(x) = x^3 - 2x^2 + 4")
plt.scatter(iteraciones_x, [funcion(x) for x in iteraciones_x], color='red', label="Iteraciones", marker='o')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Método Newton-Raphson")
plt.legend()
plt.grid(True)
plt.show()
